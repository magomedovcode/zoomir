from drf_spectacular.utils import extend_schema
from shop.models import Product
from shop.serializers import ProductDetailSerializer
from rest_framework import (
    generics,
    permissions
)


@extend_schema(tags=['Товары'])
class ProductDetailView(generics.RetrieveAPIView):
    """
    Получение детальной информации о товаре
    """
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.AllowAny]

    queryset = Product.objects.select_related(
        'brand',
        'country',
        'product_category'
    ).prefetch_related(
        'product_variants__product_images',
        'product_variants__attributes__attribute_category',
        'reviews__user'
    ).all()
