from drf_spectacular.utils import extend_schema
from shop.models import Review
from shop.serializers import ReviewSerializer
from rest_framework import (
    generics,
    permissions
)


@extend_schema(tags=['Отзывы'])
class ReviewDeleteView(generics.DestroyAPIView):
    """
    Удаление отзыва по ID для конкретного товара
    """
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Ограничиваем queryset отзывами текущего пользователя
        и только в рамках указанного товара.
        """
        product_id = self.kwargs['product_id']
        return Review.objects.filter(
            product_id=product_id,
            user=self.request.user
        )
