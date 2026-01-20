from app.models import Exercice
from rest_framework import serializers

class ExerciceSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Exercice
        fields = "__all__"
        
