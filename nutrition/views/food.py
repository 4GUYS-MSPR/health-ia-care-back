from rest_framework.viewsets import ModelViewSet

from nutrition.models import Food
from nutrition.serializers import FoodSerializer

class FoodViewSet(ModelViewSet):
    serializer_class = FoodSerializer

    def get_queryset(self):
        return Food.objects.all()
