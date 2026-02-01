from rest_framework import serializers

from app.models import Objective

class ObjectiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Objective
        fields = ["id", "value"]
