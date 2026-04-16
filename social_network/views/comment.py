from rest_framework.viewsets import ModelViewSet

from social_network.models import Comment
from social_network.serializers import CommentSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)
