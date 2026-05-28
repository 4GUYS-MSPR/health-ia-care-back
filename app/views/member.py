from rest_framework.viewsets import ModelViewSet

from app.models.member import Member
from app.serializers.member import MemberSerializer

from core.utils.query import get_query_all_for_user

class MemberViewSet(ModelViewSet):
    serializer_class = MemberSerializer

    def perform_create(self, serializer: MemberSerializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return get_query_all_for_user(Member, self.request.user)
