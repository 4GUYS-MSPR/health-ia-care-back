from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from app.models import Member
from app.serializers.member import MemberSerializer


class MemberViewSet(ModelViewSet):
    serializer_class = MemberSerializer

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_superuser:
            return Member.objects.all()
        return Member.objects.filter(client=current_user)
