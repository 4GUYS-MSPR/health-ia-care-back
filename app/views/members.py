from rest_framework.viewsets import ModelViewSet

from app.models import Member
from app.serializers.member import MemberSerializer
from app.utils.query import getQueryALLForUser


class MemberViewSet(ModelViewSet):
    serializer_class = MemberSerializer

    def get_queryset(self):
        return getQueryALLForUser(Member, self.request.user)
