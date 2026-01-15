from app.models.body_part import BodyPart
from app.models.category import Category
from app.models.equipment import Equipment
from app.models.exercice import ExerciceScheme
from app.models.muscle import Muscle

from app.utils.validation import validate_fields_fata
from app.utils.response import JsonResponse

from . import BaseAction

class ExerciceAction(BaseAction):

    def __init__(self):
        super().__init__(ExerciceScheme)

    def handle(self, data):
        fields = [
            {"name": "targetMuscles", "model": Muscle, "enum": True},
            {"name": "secondaryMuscles", "model": Muscle, "enum": True},
            {"name": "equipments", "model": Equipment, "enum": True},
            {"name": "bodyParts", "model": BodyPart, "enum": True},
            {"name": "exerciseType", "model": Category, "enum": False},
        ]
        invalid_value = validate_fields_fata(data, fields)
        if invalid_value:
            return JsonResponse.errors({"count": len(invalid_value)})
        return JsonResponse.success({"message": "All good !"})
