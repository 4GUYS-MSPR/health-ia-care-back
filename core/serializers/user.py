from rest_framework import serializers

from core.utils.user import User

class UserSerializer(serializers.ModelSerializer):
    member_id = serializers.ReadOnlyField(source='member.id')

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'member_id']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_staff': {'read_only': True},
            'member_id': {'read_only': True},
        }

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }
