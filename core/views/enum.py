import json

from enum import Enum, EnumMeta

from django.core import serializers
from django.db.models import Model
from django.http import HttpRequest
from django.utils.module_loading import import_string

from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from core.utils.logger import logger
from core.utils.response import JsonResponse

class ModelMeta(EnumMeta):
    def __contains__(cls, item):
        return isinstance(item, str) and item in cls._member_names_

class ModelEnum(str, Enum, metaclass=ModelMeta):
    Activity = "nutrition.models.activity.Activity"
    Allergie = "nutrition.models.allergie.Allergie"
    BodyPart = "app.models.body_part.BodyPart"
    ExerciceCategory = "app.models.category.Category"
    DietaryRestiction = "nutrition.models.dietary_restriction.DietaryRestiction"
    DiseaseType = "nutrition.models.disease_type.DiseaseType"
    Equipment = "app.models.equipment.Equipment"
    FoodCategory = "nutrition.models.category.Category"
    Gender = "app.models.gender.Gender"
    Level = "app.models.level.Level"
    MealType = "nutrition.models.meal_type.MealType"
    Muscle = "app.models.muscle.Muscle"
    PreferedCuisine = "nutrition.models.prefered_cuisine.PreferedCuisine"
    Recommendation = "nutrition.models.recommendation.Recommendation"
    Severity = "nutrition.models.severity.Severity"
    Subscription = "app.models.subscription.Subscription"

class EnumViewSet(ViewSet):

    def list(self, _):
        return JsonResponse.success([m.name for m in ModelEnum])

    @action(detail=False, methods=['get'], url_path='(?P<model>[^/.]+)')
    def get_enum(self, request: HttpRequest, model = None):
        if model not in ModelEnum:
            logger.log.error("Invalid model")
            return JsonResponse.response({
                "message": "Invalid model",
                "input": model
            }, 400)

        try:
            django_model: Model = import_string(ModelEnum[model])
        except ImportError:
            return JsonResponse.response({"message": f"{model} not found."}, 404)
        
        data = [
            {
                "id": obj.pk,
                "value": obj.value,
                "create_at": obj.create_at.isoformat() if obj.create_at else None
            }
            for obj in django_model.objects.all()
        ]

        return JsonResponse.response(data, 200)
