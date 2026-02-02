from rest_framework import serializers

from app.models import Session
from app.serializers.exercice import ExerciceSerializer

class SessionSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        rep['exercices'] = ExerciceSerializer(instance.exercices, many=True).data if instance.exercices else []

        return rep

    class Meta:
        model = Session
        fields = [
            "id",
            "calories_burned",
            "duration",
            "avg_bpm",
            "max_bpm",
            "resting_bpm",
            "water_intake",
            "exercices",
            "member",
            "create_at"
        ]
        read_only_fields = ["client"]
