from rest_framework.viewsets import ModelViewSet

from core.utils.query import get_query_all_for_user

from nutrition.models import Food
from nutrition.serializers import FoodSerializer

class FoodViewSet(ModelViewSet):
    serializer_class = FoodSerializer

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

    def get_queryset(self):
        return get_query_all_for_user(Food, self.request.user)
