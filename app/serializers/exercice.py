from rest_framework import serializers

from app.models import Exercice

from app.serializers.body_part import BodyPartSerializer
from app.serializers.category import CategorySerializer
from app.serializers.equipment import EquipmentSerializer
from app.serializers.muscle import MuscleSerializer

class ExerciceSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        rep['category'] = CategorySerializer(instance.category).data if instance.category else None
        rep['body_parts'] = BodyPartSerializer(instance.body_parts, many=True).data if instance.body_parts else []
        rep['equipments'] = EquipmentSerializer(instance.equipments, many=True).data if instance.equipments else []
        rep['target_muscles'] = MuscleSerializer(instance.target_muscles, many=True).data if instance.target_muscles else []
        rep['secondary_muscles'] = MuscleSerializer(instance.secondary_muscles, many=True).data if instance.secondary_muscles else []

        return rep

    class Meta:
        model = Exercice
        fields = "__all__"
        read_only_fields = ["client"]
