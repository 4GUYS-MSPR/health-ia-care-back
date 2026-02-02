from rest_framework import serializers

from nutrition.models import MealType

class MealTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = MealType
        fields = ["id", "value"]
