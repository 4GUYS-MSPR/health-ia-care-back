from rest_framework.viewsets import ModelViewSet

from app.models import Food
from app.serializers.food import FoodSerializer
from app.utils.query import getQueryALLForUser

class FoodViewSet(ModelViewSet):
    serializer_class = FoodSerializer

    def get_queryset(self):
        return getQueryALLForUser(Food, self.request.user)
