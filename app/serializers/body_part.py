from rest_framework import serializers

from app.models import BodyPart

class BodyPartSerializer(serializers.ModelSerializer):

    class Meta:
        model = BodyPart
        fields = ["id", "value"]
