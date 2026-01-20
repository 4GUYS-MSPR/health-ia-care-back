from rest_framework.viewsets import ModelViewSet
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
        queryset = Exercice.objects.all()
        for filter_name in self.filters:
            filter_value = self.request.GET.get(filter_name)
            if filter_value:
                self.query_filter[filter_name] = filter_value
        if not self.query_filter:
            return queryset
        return queryset.filter(**self.query_filter)
