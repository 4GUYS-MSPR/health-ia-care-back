from rest_framework import serializers

from app.models import Exercice

from app.serializers.body_part import BodyPartSerializer
from app.serializers.category import CategorySerializer
from app.serializers.equipment import EquipmentSerializer
from app.serializers.muscle import MuscleSerializer

class ExerciceSerializer(serializers.ModelSerializer):

    body_parts = BodyPartSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    equipments = EquipmentSerializer(many=True, read_only=True)
    target_muscles = MuscleSerializer(many=True, read_only=True)
    secondary_muscles = MuscleSerializer(many=True, read_only=True)

    class Meta:
        model = Exercice
        fields = "__all__"
