from drf_spectacular.utils import extend_schema
from shop.serializers import FavoriteProductCreateSerializer
from rest_framework import (
    generics,
    permissions
)


@extend_schema(tags=['Избранное'], request=FavoriteProductCreateSerializer)
class FavoriteProductCreateView(generics.CreateAPIView):
    """
    Добавление товара в избранное
    """
    serializer_class = FavoriteProductCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
