from rest_framework.viewsets import ModelViewSet

from core.utils.query import get_query_all_for_user

from nutrition.models import DietRecommendation
from nutrition.serializers import DietRecommendationSerializer

class DietRecommendationViewSet(ModelViewSet):
    serializer_class = DietRecommendationSerializer

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

    def get_queryset(self):
        return get_query_all_for_user(DietRecommendation, self.request.user)
