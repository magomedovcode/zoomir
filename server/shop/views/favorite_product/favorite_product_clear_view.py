from drf_spectacular.utils import extend_schema
from rest_framework import (
    generics,
    permissions,
    status
)
from rest_framework.response import Response
from shop.models import FavoriteProduct


@extend_schema(tags=['Избранное'])
class FavoriteProductClearView(generics.DestroyAPIView):
    """
    Удаление всех товаров из избранного текущего пользователя
    """
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        favorites = FavoriteProduct.objects.filter(user=request.user)
        count = favorites.count()
        favorites.delete()
        return Response(
            {"detail": f"{count} избранных товаров удалено."},
            status=status.HTTP_204_NO_CONTENT
        )
