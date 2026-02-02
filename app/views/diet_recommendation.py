from rest_framework.viewsets import ModelViewSet

from app.models import DietRecommendation
from app.serializers.diet_recommendation import DietRecommendationSerializer
from app.utils.query import getQueryALLForUser

class DietRecommendationViewSet(ModelViewSet):
    serializer_class = DietRecommendationSerializer

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

    def get_queryset(self):
        return getQueryALLForUser(DietRecommendation, self.request.user)
