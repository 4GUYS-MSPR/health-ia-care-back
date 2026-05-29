import torch
import torch.nn as nn
import torch.optim as optim

from app.models.member import Member
from app.serializers.member import MemberSerializer

from core.utils.logger import logger
from core.utils.response import JsonResponse

from ia_engine.engine import IA

def train():
    ia = IA()
    logger.log.info("📡 Récupération des profils depuis l'API Rest...")
    try:
        members = MemberSerializer(
            Member.objects.all(),
            many=True,
        ).data
    except Exception as e:
        logger.log.error(f"🛑 Le script s'est arrêté à cause de : {e}")
        return JsonResponse.error(e)

    if not members:
        logger.log.warning("⚠️ Aucun membre retourné par l'API.")
        return JsonResponse.response("Aucun membre trouvé.", 422)

    inputs, targets = [], []

    for m in members:
        # Traitement de l'objectif
        obj_str = m["objective"]["value"]
        id_obj = ia.extraire_id_objectif_ia(obj_str)

        # Extraction des features brutes
        age = float(m["age"])
        bmi = float(m["bmi"])
        fat = float(m["fat_percentage"])
        freq = float(m["workout_frequency"])

        # Normalisation
        features = [
            id_obj,
            age / ia.MAX_VALS["age"],
            bmi / ia.MAX_VALS["bmi"],
            fat / ia.MAX_VALS["fat"],
            freq / ia.MAX_VALS["freq"]
        ]

        # Simulation d'une règle cible (Target) pour que l'IA apprenne la corrélation
        if id_obj == 0.0:  # FAMILLE SURPLUS / PRISE DE MUSCLE / MASSE
            if bmi < 18.5 or fat < 10.0:
                target = 0  # 📉 Métabolisme à relancer (Profil trop sec ou sous-poids)
            elif fat > 22.0:
                target = 1  # 🛑 Excès de gras (Même avec un petit BMI, on stoppe le surplus)
            elif freq >= 5 and age < 35:
                target = 0  # 🏃‍♂️ Jeune qui s'entraîne massivement -> Besoin de plus d'énergie
            else:
                target = 2  # 🎯 Profil équilibré

        elif id_obj == 1.0:  # FAMILLE DÉFICIT / PERTE DE POIDS / SÈCHE
            if fat > 25.0 or (bmi > 25.0 and fat > 18.0):
                target = 1  # 🛑 Profil en surcharge (Le déficit est totalement cohérent)
            elif bmi < 19.0 or fat < 12.0:
                target = 0  # 📉 Danger (Déjà trop mince/sec pour vouloir perdre du poids)
            elif freq <= 0:
                target = 1  # 🛑 Sédentaire complet (Besoin de réduire la balance calorique)
            else:
                target = 2  # 🎯 Profil équilibré

        else:  # FAMILLE MAINTENANCE / PERFORMANCE / BIEN-ÊTRE
            if freq >= 5 and fat < 13.0:
                target = 0  # 🏃‍♂️ Athlète très actif et sec (Besoin de plus de carburant pour la perf)
            elif fat > 28.0:
                target = 1  # 🛑 Profil sédentaire ou en surpoids gras latent -> Il faut réguler
            elif age > 50 and freq < 2:
                target = 1  # ⏳ Senior sédentaire (Le métabolisme ralentit, attention aux excès)
            else:
                target = 2  # 🎯 Profil équilibré

        inputs.append(features)
        targets.append(target)

    # Conversion en tenseurs
    X = torch.tensor(inputs, dtype=torch.float32)
    Y = torch.tensor(targets, dtype=torch.long)

    # Entraînement
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(ia.engine.parameters(), lr=0.01)

    count = len(inputs)

    logger.log.info(f"🏋️‍♂️ Entraînement de l'IA sur {count} profils...")
    ia.engine.train()
    for _ in range(1000):
        optimizer.zero_grad()
        outputs = ia.engine(X)
        loss = criterion(outputs, Y)
        loss.backward()
        optimizer.step()

    # Sauvegarde directe dans MongoDB
    ia.save_model_to_mongo()

    return JsonResponse.success(f"Ia entraînée  sur {count} membre{'s' if count > 1 else ''}.")
