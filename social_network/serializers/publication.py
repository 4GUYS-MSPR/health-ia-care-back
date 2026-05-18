from rest_framework import serializers

from core.serializers import UserSerializer

from social_network.models.publication import Publication

class PublicationSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    comments = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    video = serializers.SerializerMethodField()

    class Meta:
        model = Publication
        fields = ["id", "user", "description", "type", "image", "video", "created_at", "comments", "likes"]

    def get_comments(self, obj: Publication):
        return obj.comments.count()

    def get_likes(self, obj: Publication):
        return obj.likes.count()

    def get_image(self, obj: Publication):
        return obj.image.url if obj.image else None

    def get_video(self, obj: Publication):
        return obj.video.url if obj.video else None
