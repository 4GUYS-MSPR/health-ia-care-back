import random
import torch
import torch.nn as nn
import torch.optim as optim

from app.models import Gender, Level, Member, Objective, Subscription
from app.serializers import GenderSerializer, LevelSerializer, MemberSerializer, ObjectiveSerializer, SubscriptionSerializer

from core.utils.logger import logger
from core.utils.response import JsonResponse

from ia_engine.engine import IA

def train():
    ia = IA()
    logger.log.info("IA | 📡 Récupération des profils depuis l'API Rest...")

    members = generate_members_json()

    if not members:
        logger.log.warning("IA | ⚠️ Aucun membre retourné par l'API.")
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

    logger.log.info(f"IA | 🏋️‍♂️ Entraînement de l'IA sur {count} profils...")
    ia.engine.train()
    for _ in range(1000):
        optimizer.zero_grad()
        outputs = ia.engine(X)
        loss = criterion(outputs, Y)
        loss.backward()
        optimizer.step()

    # Sauvegarde directe dans MongoDB
    ia.save_model_to_mongo()

    logger.log.success(f"IA | Ia entraînée sur {count} membre{'s' if count > 1 else ''}.")
    return JsonResponse.success(f"Ia entraînée sur {count} membre{'s' if count > 1 else ''}.")

def generate_members_json(count=500):
    """
    Génère un fichier JSON contenant 'count' membres réalistes 
    prêts à être injectés ou testés dans ton backend Django.
    """

    objectives = ObjectiveSerializer(Objective.objects.all(), many=True).data
    genders = GenderSerializer(Gender.objects.all(), many=True).data
    levels = LevelSerializer(Level.objects.all(), many=True).data
    subscriptions = SubscriptionSerializer(Subscription.objects.all(), many=True).data

    members = []

    logger.log.info(f"⚡ Génération de {count} membres en cours...")

    for _ in range(1, count + 1):
        obj = random.choice(objectives)
        gender = random.choice(genders)

        if obj in ["MASS_GAIN", "GAIN_MUSCLE"]:
            age = random.randint(18, 35)
            height = random.randint(170, 195) if gender == "MALE" else random.randint(160, 180)
            # Plutôt mince de base pour une prise de masse, ou standard
            bmi = round(random.uniform(17.5, 24.0), 1) 
            fat_percentage = round(random.uniform(9.0, 16.0), 1) if gender == "MALE" else round(random.uniform(18.0, 24.0), 1)
            workout_frequency = random.randint(3, 6)
            level = "EXPERT" if workout_frequency > 5 else "INTERMEDIATE" if workout_frequency > 2 else "BEGINNER"

        elif obj in ["FAT_LOSS", "WEIGHT_LOSS"]:
            age = random.randint(25, 60)
            height = random.randint(165, 188) if gender == "MALE" else random.randint(155, 175)
            # BMI en surpoids ou obésité modérée
            bmi = round(random.uniform(25.5, 34.0), 1)
            fat_percentage = round(random.uniform(24.0, 35.0), 1) if gender == "MALE" else round(random.uniform(32.0, 42.0), 1)
            workout_frequency = random.randint(0, 3)
            level = "BEGINNER"

        elif obj == "ENDURANCE_PREP":
            age = random.randint(22, 48)
            height = random.randint(168, 185)
            # Profil affûté et léger
            bmi = round(random.uniform(19.5, 22.5), 1)
            fat_percentage = round(random.uniform(8.0, 12.0), 1) if gender == "MALE" else round(random.uniform(15.0, 20.0), 1)
            workout_frequency = random.randint(4, 7)
            level = "EXPERT"

        else: # MAINTENANCE, TONING, HEALTH_HEART
            age = random.randint(30, 70) if obj == "HEALTH_HEART" else random.randint(20, 50)
            height = random.randint(160, 190)
            bmi = round(random.uniform(21.0, 25.0), 1)
            fat_percentage = round(random.uniform(14.0, 22.0), 1) if gender == "MALE" else round(random.uniform(22.0, 30.0), 1)
            workout_frequency = random.randint(1, 4)
            level = random.choice(levels)

        weight = round(bmi * ((height / 100) ** 2), 1)

        member_json = {
            "age": age,
            "bmi": bmi,
            "fat_percentage": fat_percentage,
            "height": float(height),
            "weight": weight,
            "workout_frequency": workout_frequency,
            "objective": obj,
            "gender": gender,
            "level": level,
            "subscription": random.choice(subscriptions)
        }

        members = members + [member_json]

    return members
