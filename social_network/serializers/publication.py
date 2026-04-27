from rest_framework import serializers

from social_network.models.comment import Comment
from social_network.models.publication import Publication
from social_network.serializers.comment import CommentSerializer

class PublicationSerializer(serializers.ModelSerializer):

    comments = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    video = serializers.SerializerMethodField()

    class Meta:
        model = Publication
        fields = ["id", "description", "type", "image", "video", "created_at", "comments"]

    def get_comments(self, obj: Publication):
        return CommentSerializer(Comment.objects.filter(publication_id=obj.pk), many=True).data

    def get_image(self, obj: Publication):
        return obj.image.url if obj.image else None

    def get_video(self, obj: Publication):
        return obj.video.url if obj.video else None
