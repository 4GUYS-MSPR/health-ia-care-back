from rest_framework import serializers

from core.utils.user import User

class UserSerializer(serializers.ModelSerializer):
    member_id = serializers.ReadOnlyField(source="member.id")
    avatar = serializers.SerializerMethodField()

    def get_avatar(self, obj: User):
        if hasattr(obj, 'avatar') and obj.avatar and obj.avatar.value:
            return obj.avatar.value.url
        return None

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "password", "member_id", "avatar"]
        extra_kwargs = {
            "password": {"write_only": True},
            "is_staff": {"read_only": True},
            "member_id": {"read_only": True},
        }

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {
            "password": {"write_only": True},
        }
