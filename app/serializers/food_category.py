from rest_framework import serializers

from app.models import FoodCategory

class FoodCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodCategory
        fields = ["id", "value"]
