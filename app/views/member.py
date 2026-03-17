from rest_framework.viewsets import ModelViewSet

from app.models import Member, Objective
from app.serializers.member import MemberSerializer

from core.utils.query import get_query_all_for_user

class MemberViewSet(ModelViewSet):
    serializer_class = MemberSerializer

    def perform_create(self, serializer: MemberSerializer):
        data = serializer.validated_data
        objectives = data.get('objectives')
        print(objectives)
        serializer.save(client=self.request.user)

    def perform_update(self, serializer: MemberSerializer):
        old: Member = serializer.instance
        data = serializer.validated_data
        objectives = data.get('objectives')
        print(objectives)
        for obj in Objective.objects.filter(member = old):
            if obj not in objectives:
                obj.delete()
        serializer.save()

    def get_queryset(self):
        return get_query_all_for_user(Member, self.request.user)
