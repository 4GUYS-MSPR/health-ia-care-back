from rest_framework import serializers

from nutrition.models import Allergie

class AllergieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Allergie
        fields = ["id", "value"]
