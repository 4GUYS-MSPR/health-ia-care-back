from rest_framework import serializers

from app.models import Level

class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = ["id", "value"]
