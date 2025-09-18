from shop.models import Product
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from .brand_serializer import BrandSerializer
from .country_serializer import CountrySerializer
from .product_category_serializer import ProductCategorySerializer
from .tag_serializer import TagSerializer


@extend_schema_serializer(component_name='Product')
class ProductSerializer(serializers.ModelSerializer):
    product_category = ProductCategorySerializer(
        read_only=True
    )
    brand = BrandSerializer(
        read_only=True
    )
    country = CountrySerializer(
        read_only=True
    )
    tags = TagSerializer(
        read_only=True,
        many=True
    )
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'country',
            'product_category',
            'brand',
            'tags'
        ]
        read_only_fields = fields
