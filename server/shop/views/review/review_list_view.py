from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import generics, permissions
from shop.models import Review
from shop.serializers import ReviewSerializer


@extend_schema(
    tags=['Отзывы'],
    parameters=[
        OpenApiParameter(
            name='product',
            description='ID товара',
            required=True,
            type=OpenApiTypes.INT
        )
    ]
)
class ReviewListView(generics.ListAPIView):
    """
    Список отзывов для конкретного товара
    """
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Review.objects.none()

        product_id = self.kwargs['product_id']
        return Review.objects.filter(
            product_id=product_id
        ).select_related(
            'user'
        ).prefetch_related(
            'review_photos'
        )
