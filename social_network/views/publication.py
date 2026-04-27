from rest_framework.viewsets import ModelViewSet

from social_network.serializers.publication import PublicationSerializer
from social_network.models.publication import Publication

class PublicationViewSet(ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)
