from rest_framework.viewsets import ModelViewSet

from app.models import Session
from app.serializers.session import SessionSerializer
from app.utils.query import getQueryALLForUser

class SessionViewSet(ModelViewSet):
    serializer_class = SessionSerializer

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

    def get_queryset(self):
        return getQueryALLForUser(Session, self.request.user)
