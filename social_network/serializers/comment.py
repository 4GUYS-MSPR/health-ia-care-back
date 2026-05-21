from rest_framework import serializers

from core.serializers import UserSerializer

from social_network.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(source="member.user", read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "content", "user", "created_at"]
