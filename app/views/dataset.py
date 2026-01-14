from pydantic import ValidationError
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.parsers import MultiPartParser, JSONParser

from app.models.body_part import BodyPart
from app.models.category import Category
from app.models.equipment import Equipment
from app.models.exercice import ExerciceScheme
from app.models.muscle import Muscle
from app.utils.validation import validateFieldsData
from app.utils.response import JsonResponse

class DataImportViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]

    parser_classes = [MultiPartParser, JSONParser]

    def create(self, request):
        file = request.FILES.get('file')

        if not file and not request.data:
            return JsonResponse.errors("No data")

        data = request.data
        if not isinstance(data, list):
            data = [data]

        errors = []
        exercices = []

        for _, item in enumerate(data):
            try:
                scheme = ExerciceScheme(**item)
                exercices.append(scheme)
            except ValidationError as e:
                errors.append(e.json())

        if errors:
            return JsonResponse.errors(errors)
        else:
            fields = [
                {"name": "targetMuscles", "model": Muscle, "enum": True},
                {"name": "secondaryMuscles", "model": Muscle, "enum": True},
                {"name": "equipments", "model": Equipment, "enum": True},
                {"name": "bodyParts", "model": BodyPart, "enum": True},
                {"name": "exerciseType", "model": Category, "enum": False},
            ]
            invalidValue = validateFieldsData(exercices, fields)
            if invalidValue:
                return JsonResponse.errors(invalidValue)
            else:
                return JsonResponse.success({"message": "All good !"})
