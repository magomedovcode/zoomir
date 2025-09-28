from drf_spectacular.utils import extend_schema
from rest_framework import (
    generics,
    permissions,
    status
)
from rest_framework.response import Response
from shop.models import FavoriteProduct
from shop.serializers import FavoriteProductSerializer


@extend_schema(tags=['Избранное'])
class FavoriteProductClearView(generics.DestroyAPIView):
    """
    Удаление всех товаров из избранного текущего пользователя
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FavoriteProductSerializer

    def get_queryset(self):
        return FavoriteProduct.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        self.get_queryset().delete()
        return Response(
            {"detail": "Все товары удалены из избранного"},
            status=status.HTTP_204_NO_CONTENT
        )
