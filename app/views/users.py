from django.contrib.auth.models import User
from rest_framework import viewsets

from app.serializers.user import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.all().order_by('id') if user.is_staff else User.objects.filter(id=user.id).order_by('id')
