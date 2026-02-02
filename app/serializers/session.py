from rest_framework import serializers

from app.models import Session

class SessionSerializer(serializers.ModelSerializer):

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
