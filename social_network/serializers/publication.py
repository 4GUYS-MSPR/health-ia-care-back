from rest_framework import serializers

from core.serializers import UserSerializer

from social_network.models.publication import Publication

class PublicationSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    comments = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    has_liked = serializers.SerializerMethodField()
    has_commented = serializers.SerializerMethodField()

    def to_representation(self, instance):
        ret = super().to_representation(instance)

        if instance.image:
            ret['image'] = instance.image.url
        else:
            ret['image'] = None

        if instance.video:
            ret['video'] = instance.video.url
        else:
            ret['video'] = None

        return ret

    def validate(self, attrs):
        pub_type = attrs.get('type')
        image = attrs.get('image')
        video = attrs.get('video')

        if pub_type == 1 and not image:
            raise serializers.ValidationError(
                {'image': "Can't be null for image type"}
            )

        if pub_type == 2 and not video:
            raise serializers.ValidationError(
                {'video': "Can't be null for video type"}
            )

        return attrs

    class Meta:
        model = Publication
        fields = [
            "id",
            "user",
            "description",
            "type",
            "image",
            "video",
            "created_at",
            "comments",
            "likes",
            "has_liked",
            "has_commented",
        ]

    def get_comments(self, obj: Publication):
        return obj.comments.count()

    def get_likes(self, obj: Publication):
        return obj.likes.count()

    def get_has_commented(self, obj: Publication):
        request = self.context.get('request')
        if not request or not request.user or request.user.is_anonymous:
            return False

        return obj.comments.filter(member__user=request.user).exists()

    def get_has_liked(self, obj: Publication):
        request = self.context.get('request')
        if not request or not request.user or request.user.is_anonymous:
            return False

        return obj.likes.filter(member__user=request.user).exists()
