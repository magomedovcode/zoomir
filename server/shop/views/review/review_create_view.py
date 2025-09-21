from drf_spectacular.utils import extend_schema
from shop.serializers import ReviewCreateSerializer
from rest_framework import (
    generics,
    permissions
)


@extend_schema(tags=['Отзывы'], request=ReviewCreateSerializer)
class ReviewCreateView(generics.CreateAPIView):
    """
    Создание нового отзыва от текущего пользователя
    """
    serializer_class = ReviewCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
