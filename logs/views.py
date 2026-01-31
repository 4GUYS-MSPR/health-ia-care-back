from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .models import Log
from .serializers import LogSerializer

class LogViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]

    serializer_class = LogSerializer
    queryset = Log.objects.all()
