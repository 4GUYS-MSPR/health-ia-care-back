from django.http import HttpRequest

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from app.models import Member

from social_network.serializers.publication import PublicationSerializer
from social_network.models import Like, Publication

class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post', 'delete'])
    def like(self, request: HttpRequest, pk=None): # pylint: disable=unused-argument
        publication = self.get_object()

        try:
            member = Member.objects.get(user=request.user)

            if request.method == "POST":
                Like.objects.get_or_create(publication=publication, member=member)
                publication.has_liked = True
                serializer = PublicationSerializer(publication)
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)

            if request.method == "DELETE":
                Like.objects.get(publication=publication, member=member).delete()
                publication.has_liked = False
                serializer = PublicationSerializer(publication)
                return Response(data=serializer.data, status=status.HTTP_200_OK)

            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        except Member.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data="Member not found")
