from rest_framework import serializers

from app.models import DiseaseType

class DiseaseTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DiseaseType
        fields = ["id", "value"]
