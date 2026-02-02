from rest_framework import serializers

from app.models import DietaryRestriction

class DietaryRestrictionSerializer(serializers.ModelSerializer):

    class Meta:
        model = DietaryRestriction
        fields = ["id", "value"]
