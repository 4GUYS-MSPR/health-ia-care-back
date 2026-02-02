from rest_framework import serializers

from nutrition.models import Severity

class SeveritySerializer(serializers.ModelSerializer):

    class Meta:
        model = Severity
        fields = ["id", "value"]
