from app.models.exercice import Exercice
from app.models.category import Category
from app.models.body_part import BodyPart
from app.models.equipment import Equipment
from app.models.muscle import Muscle

import datetime


def create_exercice(client, **kwargs):
    body_part, _ = BodyPart.objects.get_or_create(value = "FACE", create_at = datetime.datetime.now())
    category, _ = Category.objects.get_or_create(value = "YOGA", create_at = datetime.datetime.now())
    equipment, _ = Equipment.objects.get_or_create(value = "STICK", create_at = datetime.datetime.now())
    muscle, _ = Muscle.objects.get_or_create(value = "SPLENIUS", create_at = datetime.datetime.now())

    defaults = {
        "image_url" : "https://image.com",
        "category" : category,
        "client" : client,
        "create_at" : datetime.datetime.now()
    }
    defaults.update(kwargs)

    exercice = Exercice.objects.create(**defaults)

    exercice.body_parts.set([body_part])
    exercice.equipments.set([equipment])
    exercice.target_muscles.set([muscle])
    exercice.secondary_muscles.set([muscle])

    return exercice
