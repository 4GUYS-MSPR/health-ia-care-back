from rest_framework.viewsets import ModelViewSet

from core.utils.query import getQueryALLForUser

from nutrition.models import Food
from nutrition.serializers import FoodSerializer

class FoodViewSet(ModelViewSet):
    serializer_class = FoodSerializer

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

    def get_queryset(self):
        return getQueryALLForUser(Food, self.request.user)
