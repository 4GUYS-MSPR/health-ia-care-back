from rest_framework.viewsets import ModelViewSet

from app.models import Member
from app.serializers.member import MemberSerializer

from core.utils.query import getQueryALLForUser

class MemberViewSet(ModelViewSet):
    serializer_class = MemberSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        serializer.save(client=self.request.user)

    def get_queryset(self):
        return getQueryALLForUser(Member, self.request.user)
