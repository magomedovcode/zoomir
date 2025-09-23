from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from shop.serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework import (
    generics,
    permissions,
    status
)


@extend_schema(tags=['Пользователь'])
class RegisterView(generics.CreateAPIView):
    """
    Регистрация нового пользователя по логину и паролю
    """
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        data = {
            "id": user.id,
            "username": user.username,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return Response(data, status=status.HTTP_201_CREATED)
