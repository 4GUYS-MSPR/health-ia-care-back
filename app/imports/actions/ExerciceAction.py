from . import BaseAction

from app.models.body_part import BodyPart
from app.models.category import Category
from app.models.equipment import Equipment
from app.models.exercice import ExerciceScheme
from app.models.muscle import Muscle

class ExerciceAction(BaseAction):

    def __init__(self):
        super().__init__(ExerciceScheme)

    def handle(self):
        fields = [
            {"name": "targetMuscles", "model": Muscle, "enum": True},
            {"name": "secondaryMuscles", "model": Muscle, "enum": True},
            {"name": "equipments", "model": Equipment, "enum": True},
            {"name": "bodyParts", "model": BodyPart, "enum": True},
            {"name": "exerciseType", "model": Category, "enum": False},
        ]
        invalidValue = validateFieldsData(exercices, fields)
        if invalidValue:
            return JsonResponse.errors({"count": len(invalidValue)})
        else:
            return JsonResponse.success({"message": "All good !"})
