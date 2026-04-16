from django.utils import timezone

from rest_framework.viewsets import ModelViewSet

from app.models import Member, Objective
from app.serializers.member import MemberSerializer

from core.utils.query import get_query_all_for_user

class MemberViewSet(ModelViewSet):
    serializer_class = MemberSerializer

    def perform_create(self, serializer: MemberSerializer):
        data = serializer.validated_data
        objectives = data.pop('objectives')
        member = serializer.save(client=self.request.user)
        for obj in objectives:
            Objective.objects.create(
                member=member,
                value=obj.get('value'),
                create_at=timezone.now()
            )

    def perform_update(self, serializer: MemberSerializer):
        old: Member = serializer.instance
        data = serializer.validated_data
        objectives = data.pop('objectives')
        avalaible = Objective.objects.filter(member = old)
        serializer.save()
        for obj in objectives:
            if obj not in avalaible:
                Objective.objects.create(
                    member=old,
                    value=obj.get('value'),
                    create_at=timezone.now()
                )
            else:
                model = avalaible.get(id=obj.get('id'))
                model.value = obj.get('value')
                model.save()

        for obj in avalaible:
            if obj not in objectives:
                obj.delete()

    def get_queryset(self):
        return get_query_all_for_user(Member, self.request.user)
