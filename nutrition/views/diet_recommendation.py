from rest_framework.viewsets import ModelViewSet

from core.utils.query import getQueryALLForUser

from nutrition.models import DietRecommendation
from nutrition.serializers import DietRecommendationSerializer

class DietRecommendationViewSet(ModelViewSet):
    serializer_class = DietRecommendationSerializer

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

    def get_queryset(self):
        return getQueryALLForUser(DietRecommendation, self.request.user)
