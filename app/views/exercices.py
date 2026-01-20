from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from app.models import Exercice
from app.serializers.exercice import ExerciceSerializer

class ExerciceViewSet(ModelViewSet):
    serializer_class = ExerciceSerializer

    filters = [
        "category",
        "equipments",
        "target_muscles",
        "body_parts"
    ]

    query_filter = {}

    def get_queryset(self):
        queryset= Exercice.objects.all()
        for filter in self.filters:
            if self.request.GET.get(filter):
                self.query_filter[filter] = self.request.GET.get(filter)
        if len(self.query_filter) == 0:
            return queryset
        return queryset.filter(**self.query_filter)
        