from rest_framework import serializers

from app.models import Food

from app.serializers.food_category import FoodCategorySerializer
from app.serializers.meal_type import MealTypeSerializer

class FoodSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        rep['category'] = FoodCategorySerializer(instance.category).data if instance.category else None
        rep['meal_type'] = MealTypeSerializer(instance.meal_type).data if instance.meal_type else None

        return rep

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
        read_only_fields = ["client"]
