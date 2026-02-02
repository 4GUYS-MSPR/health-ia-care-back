from rest_framework import serializers

from nutrition.models import PreferredCuisine

class PreferredCuisineSerializer(serializers.ModelSerializer):

    class Meta:
        model = PreferredCuisine
        fields = ["id", "value"]
