from rest_framework import serializers

from core.serializers import UserSerializer

from logs.models import Log

class LogSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Log
        fields = '__all__'
