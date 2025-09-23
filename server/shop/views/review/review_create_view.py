from drf_spectacular.utils import extend_schema
from shop.serializers import ReviewCreateSerializer
from rest_framework import (
    generics,
    permissions
)


@extend_schema(tags=['Отзывы'])
class ReviewCreateView(generics.CreateAPIView):
    """
    Создание отзыва для конкретного товара
    """
    serializer_class = ReviewCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        product_id = self.kwargs['product_id']
        serializer.save(product_id=product_id, user=self.request.user)
