from rest_framework import serializers

from app.models import Food

from app.serializers.food_category import FoodCategorySerializer
from app.serializers.meal_type import MealTypeSerializer

class FoodSerializer(serializers.ModelSerializer):

    category = FoodCategorySerializer(read_only=True)
    meal_type = MealTypeSerializer(read_only=True)

    class Meta:
        model = Food
        fields = [
            "id",
            "label",
            "calories",
            "protein",
            "carbohydrates",
            "fat",
            "fiber",
            "sugars",
            "sodium",
            "cholesterol",
            "water_intake",
            "category",
            "meal_type",
            "create_at"
        ]
