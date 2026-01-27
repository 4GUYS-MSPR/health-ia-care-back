from app.models.body_part import BodyPart
from app.models.category import Category
from app.models.equipment import Equipment
from app.models.exercice import Exercice, ExerciceScheme
from app.models.muscle import Muscle

from app.utils.response import JsonResponse
from app.utils.types import AnyUser
from app.utils.validation import validate_fields_data

from . import BaseAction

class ExerciceAction(BaseAction):

    def __init__(self, user: AnyUser):
        super().__init__(ExerciceScheme, user)

    def handle(self, data: list[ExerciceScheme]):
        fields = [
            {"name": "targetMuscles", "model": Muscle, "is_list": True},
            {"name": "secondaryMuscles", "model": Muscle, "is_list": True},
            {"name": "equipments", "model": Equipment, "is_list": True},
            {"name": "bodyParts", "model": BodyPart, "is_list": True},
            {"name": "exerciseType", "model": Category, "is_list": False},
        ]
        invalid_value = validate_fields_data(data, fields)
        if invalid_value:
            return JsonResponse.errors({"fields": invalid_value})

        for scheme in data:
            from loguru import logger
            logger.debug(scheme.model_dump())

            bodyParts = BodyPart.objects.filter(value__in=self.upper(scheme.bodyParts))
            equipments = Equipment.objects.filter(value__in=self.upper(scheme.equipments))
            category = Category.objects.get(value=self.upper(scheme.exerciseType))
            secondaryMuscles = Muscle.objects.filter(value__in=self.upper(scheme.secondaryMuscles))
            targetMuscles = Muscle.objects.filter(value__in=self.upper(scheme.targetMuscles))

            exercice, _ = Exercice.objects.get_or_create(
                image_url=scheme.imageUrl,
                category=category,
            )
            exercice.body_parts.set(bodyParts)
            exercice.equipments.set(equipments)
            exercice.secondary_muscles.set(secondaryMuscles)
            exercice.target_muscles.set(targetMuscles)
            exercice.save()

        return JsonResponse.success({"message": f"{len(data)} row{'s' if len(data) > 1 else ''} imported !"})
