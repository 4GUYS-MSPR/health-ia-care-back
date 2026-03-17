from rest_framework.viewsets import ModelViewSet

from app.models import Session
from app.serializers.session import SessionSerializer

from core.utils.query import get_query_all_for_user

class SessionViewSet(ModelViewSet):
    serializer_class = SessionSerializer

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

    def get_queryset(self):
        return get_query_all_for_user(Session, self.request.user)
