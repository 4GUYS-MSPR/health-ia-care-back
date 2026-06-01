import io
import torch
import torch.nn as nn

from sklearn.metrics import classification_report, confusion_matrix

from app.models.member import Member
from app.serializers.member import MemberSerializer

from core.utils.logger import logger

from ia_engine.database import DB

class IA:
    _instance = None
    engine = None

    model_name="nutrition_model"
    
    # Constantes de normalisation pour les 7 entrées de l'IA
    MAX_VALS = {
        "age": 100.0, "bmi": 50.0, "fat": 100.0, 
        "height": 250.0, "weight": 200.0, "freq": 10.0
    }

    # On mappe chaque objectif sur une valeur numérique claire pour les mathématiques de l'IA
    MAPPING_OBJECTIFS_IA = {
        # Famille 0 : Besoin de surplus / Construction
        "GAIN_MUSCLE": 0.0,
        "MASS_GAIN": 0.0,

        # Famille 1 : Besoin de déficit / Réduction
        "FAT_LOSS": 1.0,
        "WEIGHT_LOSS": 1.0,

        # Famille 2 : Maintenance / Énergie / Performance
        "MAINTENANCE": 2.0,
        "ENDURANCE_PREP": 2.0,
        "HEALTH_HEART": 2.0,
        "TONING": 2.0
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            cls._instance.engine = cls._instance.load_model_from_mongo()

        return cls._instance

    # Si un nouvel objectif arrive et n'est pas reconnu, on le met en maintenance par défaut
    def extraire_id_objectif_ia(self, objective_value):
        return self.MAPPING_OBJECTIFS_IA.get(objective_value, 2.0)

    # =============================================
    # ARCHITECTURE DE L'IA (7 ENTRÉES -> 3 CLASSES)
    # =============================================
    class MemberProfileClassifier(nn.Module):
        def __init__(self):
            super().__init__()
            # 5 entrées : objective_id, age, bmi, fat_percentage, workout_frequency
            self.network = nn.Sequential(
                nn.Linear(5, 32),
                nn.ReLU(),
                nn.Linear(32, 3) # 0: Métabolisme Lent, 1: Métabolisme Rapide, 2: Profil Équilibré
            )

        def forward(self, x):
            return self.network(x)

    # =====================================
    # SAUVEGARDE ET CHARGEMENT DEPUIS MONGO
    # =====================================
    def save_model_to_mongo(self):
        """Convertit les poids du modèle en binaire et les stocke dans MongoDB"""
        mongo = DB()
        buffer = io.BytesIO()
        torch.save(self.engine.state_dict(), buffer)
        binaire_model = buffer.getvalue()

        # On met à jour ou on insère le modèle dans la collection 'ai_models'
        mongo.db["ai_models"].update_one(
            {"name": self.model_name},
            {"$set": {"weights": binaire_model}},
            upsert=True
        )
        mongo.close()
        logger.log.success("IA | 💾 Les poids de l'IA ont été sauvegardés avec succès dans MongoDB !")

    def load_model_from_mongo(self):
        """Récupère le binaire depuis MongoDB et reconstruit le modèle PyTorch"""
        mongo = DB()
        doc = mongo.db["ai_models"].find_one({"name": self.model_name})
        mongo.close()

        self.engine = self.MemberProfileClassifier()

        if doc and "weights" in doc:
            buffer = io.BytesIO(doc["weights"])
            self.engine.load_state_dict(torch.load(buffer, map_location=torch.device('cpu')))
            logger.log.info("IA | 🔄 Modèle chargé depuis MongoDB.")
        else:
            logger.log.info("IA | 🆕 Aucun modèle trouvé dans MongoDB. Utilisation d'un modèle vierge.")
        return self.engine

    def get_total_members_count(self):
        """Récupère le nombre total de membres dans la collection MongoDB"""
        mongo = DB()
        total_membres = mongo.db["members"].count_documents({}) 
        logger.log.info(f"IA | 👥 {total_membres} membres trouvés dans la base de données MongoDB.")
        mongo.close()
        return total_membres

    # =================================
    # CALCUL POUR L'ÉVALUATION DU MODEL
    # =================================
    def calculer_y_true_metier(self, m: dict):
        """
        Recopie exacte de la fonction cible de ton script d'entraînement.
        Garantit la cohérence scientifique pour le calcul du y_true.
        """
        obj_str = m.get("objective", {}).get("value", "MAINTENANCE")
        id_obj = self.extraire_id_objectif_ia(obj_str)

        age = float(m.get("age", 20))
        bmi = float(m.get("bmi", 20))
        fat = float(m.get("fat_percentage", 20))
        freq = float(m.get("workout_frequency", 0))

        if id_obj == 0.0:  # FAMILLE SURPLUS
            if bmi < 18.5 or fat < 10.0:
                return 0
            elif fat > 22.0:
                return 1
            elif freq >= 5 and age < 35:
                return 0
            else:
                return 2

        elif id_obj == 1.0:  # FAMILLE DÉFICIT
            if fat > 25.0 or (bmi > 25.0 and fat > 18.0):
                return 1
            elif bmi < 19.0 or fat < 12.0:
                return 0
            elif freq <= 0:
                return 1
            else:
                return 2

        else:  # FAMILLE MAINTENANCE
            if freq >= 5 and fat < 13.0:
                return 0
            elif fat > 28.0:
                return 1
            elif age > 50 and freq < 2:
                return 1
            else:
                return 2

    def evaluate(self):
        logger.log.info("IA | 📡 Récupération des membres...")

        members: list[dict] = MemberSerializer(
            Member.objects.all(),
            many=True,
        ).data

        if not members:
            logger.log.warning("IA | ⚠️ Aucun membre trouvé.")
            return

        logger.log.info("IA | 🔄 Chargement du modèle PyTorch depuis MongoDB...")
        self.engine.eval()

        y_true = []
        y_pred = []

        logger.log.info(f"IA | 🧠 Analyse de {len(members)} membres par le réseau de neurones...")

        # 2. Remplissage des vecteurs y_true et y_pred
        for m in members:
            vrai_label = self.calculer_y_true_metier(m)
            y_true.append(vrai_label)

            obj_str = m.get("objective", {}).get("value", "MAINTENANCE")
            id_obj = self.extraire_id_objectif_ia(obj_str)

            features = [
                id_obj,
                float(m.get("age", 20)) / self.MAX_VALS["age"],
                float(m.get("bmi", 20)) / self.MAX_VALS["bmi"],
                float(m.get("fat_percentage", 0)) / self.MAX_VALS["fat"],
                float(m.get("workout_frequency", 0)) / self.MAX_VALS["freq"]
            ]

            input_tensor = torch.tensor([features], dtype=torch.float32)

            with torch.no_grad():
                outputs = self.engine(input_tensor)
                prediction = torch.argmax(outputs, dim=1).item()
                y_pred.append(prediction)

        # 3. Génération des statistiques
        target_names = ['0: Forte Demande', '1: Modération', '2: Équilibré']
        labels = ['Demande (0)', 'Modere (1)', 'Equilibre (2)']

        matrix = confusion_matrix(y_true, y_pred)
        report = classification_report(y_true, y_pred, target_names=target_names, output_dict=True)

        tableau_lignes = []
        tableau_lignes.append(f"{'':<20} | {'Réel (0)':^10} | {'Réel (1)':^10} | {'Réel (2)':^10} |")
        tableau_lignes.append("-" * 60 + "|")

        for i, row in enumerate(matrix):
            tableau_lignes.append(f"{f'Prédit {labels[i]}':<20} | {row[0]:^10} | {row[1]:^10} | {row[2]:^10} |")

        tableau_lignes.append("-" * 60 + "|")
        tableau_string = "\n".join(tableau_lignes)

        logger.log.info("IA | 🎯 RAPPORT DE FIABILITÉ\n" + classification_report(y_true, y_pred, target_names=target_names))
        logger.log.info("IA | 🧩 MATRICE DE CONFUSION :\n"+ tableau_string)

        return {
            "status": "success",
            "metrics": {
                "accuracy": round(report["accuracy"], 2),
                "macro_avg": {
                    "precision": round(report["macro avg"]["precision"], 2),
                    "recall": round(report["macro avg"]["recall"], 2),
                    "f1_score": round(report["macro avg"]["f1-score"], 2)
                },
                "details_per_class": {
                    "forte_demande": report['0: Forte Demande'],
                    "moderation": report['1: Modération'],
                    "equilibre": report['2: Équilibré']
                }
            },
            "confusion_matrix": {
                "raw": matrix.tolist(),  # Convertit la matrice numpy en listes Python [ [] , [] ]
                "formatted_string": tableau_string  # Permet au front d'afficher directement ton tableau s'il le souhaite
            }
        }

    # ============================
    # MOTEUR DE PHRASES MODULAIRES
    # ============================
    def generer_recommandation_profile(self, id_status, member_data):
        phrases = []

        # 1. RÉCUPÉRATION DES METRICS DU MEMBRE
        objective = member_data.get("objectives", {}).get("value", "MAINTENANCE")
        age = int(member_data.get("age") or 20)
        bmi = float(member_data.get("bmi", 0))
        fat = float(member_data.get("fat_percentage", 0))
        freq = int(member_data.get("workout_frequency", 0))

        # 2. LA TENDANCE GLOBALE DE L'IA (id_status calculé via les poids de MongoDB)
        if id_status == 0:
            phrases.append("📉 L'analyse indique que votre organisme est en forte demande énergétique.")
        elif id_status == 1:
            phrases.append("🛑 L'analyse de vos métriques corporelles recommande une phase de modération ou de stabilisation.")
        else:
            phrases.append("🎯 L'analyse montre un excellent équilibre entre votre condition physique et votre activité.")

        # 3. ANALYSE DES COMPOSITIONS CORPORELLES (Fat & BMI)
        if fat > 25.0:
            phrases.append(f"⚖️ Avec un taux de masse grasse de {fat}%, la priorité doit être mise sur la qualité et la densité nutritionnelle plutôt que sur le volume global.")
        elif 0 < fat < 10.0:
            phrases.append(f"⚡ Votre taux de masse grasse de {fat}% est particulièrement bas, ce qui nécessite un soutien nutritionnel accru pour protéger votre capital musculaire.")

        if bmi < 18.5 and bmi > 0:
            phrases.append(f"⚠️ Votre indice de masse corporelle ({bmi}) signale un profil en sous-poids qui exige une vigilance sur vos apports quotidiens.")

        # 4. ANALYSE DU RYTHME DE VIE & DE L'ÂGE (Workout frequency & Age)
        if freq >= 5:
            phrases.append(f"🔥 Votre rythme élevé de {freq} entraînements par semaine consomme énormément de ressources musculaires et de glycogène.")
        elif freq <= 0:
            phrases.append("🛋️ Votre sédentariété actuelle limite vos dépenses quotidiennes, ce qui réduit temporairement votre tolérance aux écarts caloriques.")

        if age > 50 and id_status == 1:
            phrases.append("⏳ Avec les années, le métabolisme ralentit naturellement ; une attention plus fine sur le contrôle des portions est judicieuse.")

        # 5. CROISEMENT ET COHÉRENCE AVEC LA GRANDE LISTE D'OBJECTIFS
        # Famille Construction / Surplus
        if objective in ["GAIN_MUSCLE", "MASS_GAIN"]:
            if id_status == 1:
                phrases.append("🔄 Régulez vos macros : entamer un surplus calorique avec vos métriques actuelles risquerait de détériorer votre composition corporelle.")
            elif id_status == 0:
                phrases.append("💪 C'est le moment idéal pour accentuer vos apports en protéines et en glucides afin de maximiser l'anabolisme musculaire.")

        # Famille Perte de poids / Sèche
        elif objective in ["FAT_LOSS", "WEIGHT_LOSS"]:
            if id_status == 0:
                phrases.append("🚨 Alerte : poursuivre un déficit alors que vos voyants énergétiques sont déjà bas pourrait bloquer votre métabolisme et altérer votre santé.")
            elif id_status == 1:
                phrases.append("🥗 Votre objectif est cohérent : privilégiez un léger déficit calorique et des aliments riches en fibres pour optimiser la satiété.")

        # Objectifs spécifiques (Endurance, Santé, Tonification)
        elif objective == "ENDURANCE_PREP":
            phrases.append("🏃‍♂️ Votre préparation athlétique demande un focus majeur sur la recharge en glucides complexes pour maintenir vos stocks d'énergie.")

        elif objective == "HEALTH_HEART":
            phrases.append("❤️ Axez votre alimentation sur des acides gras de haute qualité (Oméga-3) et réduisez activement le sodium et les produits transformés.")

        elif objective == "TONING":
            phrases.append("💎 Pour sculpter votre silhouette, visez une balance calorique neutre combinée à un apport protéique strict pour tonifier le muscle.")

        # 6. SÉCURITÉ : On fusionne et on limite strictement aux 3 premières phrases les plus pertinentes
        return " ".join(phrases[:3])
