from rest_framework.viewsets import ModelViewSet

from .models import Log
from .serializers import LogSerializer

class LogViewSet(ModelViewSet):
    serializer_class = LogSerializer
    queryset = Log.objects.all()
