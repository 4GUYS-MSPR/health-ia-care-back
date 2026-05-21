from rest_framework.viewsets import ModelViewSet

from app.models import Member

from social_network.models import Comment
from social_network.serializers import CommentSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        user = self.request.user

        try:
            member = Member.objects.get(user=user)
            serializer.save(member=member)
        except Member.DoesNotExist as e:
            print(e)
