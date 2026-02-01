from rest_framework import serializers

from app.models import Equipment

class EquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipment
        fields = ["id", "value"]
