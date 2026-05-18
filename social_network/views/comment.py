from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from social_network.models import Comment
from social_network.serializers import CommentSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

    @action(detail=False, methods=['get'], url_path='get_by_publication/(?P<publication_id>[^/.]+)')
    def get_by_publication(self, request, publication_id=None):
        comments = Comment.objects.filter(publication_id=publication_id)

        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data, status=200)
