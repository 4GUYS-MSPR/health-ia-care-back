from django.db import transaction
from django.http import HttpRequest

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response

from app.models import Client, Member

from core.serializers import UserSerializer, UserCreateSerializer
from core.utils.logger import logger
from core.utils.response import JsonResponse
from core.utils.query import get_query_all_for_user
from core.utils.user import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action in ['create']:
            return UserCreateSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action in ["me"]:
            return [IsAuthenticated()]
        if self.action in ["create"]:
            return [AllowAny()]
        return [IsAdminUser()]

    def get_queryset(self):
        return get_query_all_for_user(User, self.request.user).order_by('id')

    @transaction.atomic
    def create(self, request: HttpRequest, *args, **kwargs):
        data = request.data.copy()
        client_code = data.pop('client', None)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        if client_code is not None:
            try:
                client = Client.objects.get(code=client_code)
                Member.object.create(
                    user=user,
                    client=client
                )
            except Client.DoesNotExist as e:
                logger.log.error(f"Unable to create member. Client {client_code} not found !", e)
                raise serializer.ValidationError({"client_uuid": "Client not found."})

        return JsonResponse.response(serializer.data, 201)

    @action(detail=False, methods=['get'])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
