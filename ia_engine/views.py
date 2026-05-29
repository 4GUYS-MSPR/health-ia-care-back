import torch

from django.http import HttpRequest

from sklearn.metrics import classification_report, confusion_matrix

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from app.models.member import Member
from app.serializers.member import MemberSerializer

from core.utils.logger import logger
from core.utils.response import JsonResponse

from ia_engine.engine import IA
from ia_engine.database import test
from ia_engine.train import train

class IAViewSet(viewsets.ViewSet):

    def get_permissions(self):
        if self.action in ["recommendation"]:
            return [IsAuthenticated()]
        return [IsAdminUser()]

    def list(self, _: HttpRequest):
        return JsonResponse.success([
            "evaluate",
            "recommendation",
            "test",
            "train",
        ])

    @action(detail=False, methods=['get'])
    def recommendation(self, request: HttpRequest):
        ia = IA()
        logger.log.info("🚀 Démarrage du script de test de l'IA...")

        try:
            member: dict = MemberSerializer(Member.objects.get(user=request.user)).data
        except Member.DoesNotExist:
            logger.log.error(f"Member for user={request.user.username} not found.")
            return JsonResponse.response({"message": f"Your account has not be found."}, 404)

        # 2. Extraction et normalisation des données (Préparation pour l'IA)
        obj_str = member.get("objective", {}).get("value", "GAIN_WEIGHT")
        id_obj = 0.0 if obj_str == "GAIN_WEIGHT" else 1.0

        features = [
            id_obj,
            float(member.get("age", 20)) / ia.MAX_VALS["age"],
            float(member.get("bmi", 0)) / ia.MAX_VALS["bmi"],
            float(member.get("fat_percentage", 0)) / ia.MAX_VALS["fat"],
            float(member.get("workout_frequency", 0)) / ia.MAX_VALS["freq"]
        ]

        ia.engine.eval()

        # 4. Conversion en tenseur PyTorch et calcul de la prédiction
        input_tensor = torch.tensor([features], dtype=torch.float32)

        with torch.no_grad():
            predictions_brutes = ia.engine(input_tensor)
            # On récupère l'index de la classe qui a le score le plus élevé (0, 1 ou 2)
            id_status_predit = torch.argmax(predictions_brutes, dim=1).item()

        logger.log.info(f"📊 Classe prédite par l'IA (depuis MongoDB) : {id_status_predit}")

        # 5. Passage dans le moteur modulaire pour fabriquer la phrase
        phrase_recommandation = ia.generer_recommandation_profile(id_status_predit, member)

        # 6. Affichage du résultat final
        logger.log.info("\n📝 RÉPONSE ENVOYÉE PAR L'IA :")
        logger.log.info(f"\n\"{phrase_recommandation}\"\n")
        return JsonResponse.success({"result": phrase_recommandation})

    @action(detail=False, methods=['get'])
    def evaluate(self, _: HttpRequest):
        ia = IA()
        logger.log.info("📡 Récupération des profils depuis l'API Rest...")

        members: list[dict] = MemberSerializer(
            Member.objects.all(),
            many=True,
        ).data

        if not members:
            logger.log.warning("⚠️ Aucun membre retourné par l'API.")
            return

        logger.log.info("🔄 Chargement du modèle PyTorch depuis MongoDB...")
        ia.engine.eval()

        y_true = []
        y_pred = []

        logger.log.info(f"🧠 Analyse de {len(members)} profils par le réseau de neurones...")

        # 2. Remplissage des vecteurs y_true et y_pred
        for m in members:
            vrai_label = ia.calculer_y_true_metier(m)
            y_true.append(vrai_label)

            obj_str = m.get("objective", {}).get("value", "MAINTENANCE")
            id_obj = ia.extraire_id_objectif_ia(obj_str)

            features = [
                id_obj,
                float(m.get("age", 20)) / ia.MAX_VALS["age"],
                float(m.get("bmi", 20)) / ia.MAX_VALS["bmi"],
                float(m.get("fat_percentage", 0)) / ia.MAX_VALS["fat"],
                float(m.get("workout_frequency", 0)) / ia.MAX_VALS["freq"]
            ]

            input_tensor = torch.tensor([features], dtype=torch.float32)

            with torch.no_grad():
                outputs = ia.engine(input_tensor)
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

        logger.log.info("\n🎯 RAPPORT DE FIABILITÉ\n")
        logger.log.info(classification_report(y_true, y_pred, target_names=target_names))
        logger.log.info("\n🧩 MATRICE DE CONFUSION :\n+ tableau_string")

        api_response = {
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
        return JsonResponse.success(api_response)

    @action(detail=False, methods=['get'])
    def test(self, _: HttpRequest):
        return test()

    @action(detail=False, methods=['get'])
    def train(self, _: HttpRequest):
        return train()
