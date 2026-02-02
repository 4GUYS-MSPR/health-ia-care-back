from rest_framework.viewsets import ModelViewSet

from app.models import Exercice
from app.serializers.exercice import ExerciceSerializer

from core.utils.query import getQueryALLForUser

class ExerciceViewSet(ModelViewSet):
    query_filter = {}
    serializer_class = ExerciceSerializer

    filters = [
        "category",
        "equipments",
        "target_muscles",
        "body_parts"
    ]

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

    def get_queryset(self):
        queryset = getQueryALLForUser(Exercice, self.request.user)
        for filter_name in self.filters:
            filter_value = self.request.GET.get(filter_name)
            if filter_value:
                self.query_filter[filter_name] = filter_value
        if not self.query_filter:
            return queryset
        return queryset.filter(**self.query_filter)
