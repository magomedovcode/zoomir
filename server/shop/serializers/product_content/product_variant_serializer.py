from shop.models import ProductVariant
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from shop.serializers import AttributeSerializer, ProductSerializer, ProductImageSerializer


@extend_schema_serializer(component_name='ProductVariant')
class ProductVariantSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(
        many=True,
        read_only=True
    )
    attributes = AttributeSerializer(
        many=True,
        read_only=True
    )
    product = ProductSerializer(
        read_only=True
    )
    class Meta:
        model = ProductVariant
        fields = [
            'id',
            'product',
            'name',
            'price',
            'product_images',
            'attributes',
        ]
        read_only_fields = fields
