from shop.models import ProductInOrder
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from .product_variant_serializer import ProductVariantSerializer
from rest_framework import serializers as _serializers  # to avoid confusion


@extend_schema_serializer(component_name='ProductInOrder')
class ProductInOrderSerializer(serializers.ModelSerializer):
    product_variant = ProductVariantSerializer(
        read_only=True
    )
    order = _serializers.PrimaryKeyRelatedField(read_only=True)
    cost = serializers.ReadOnlyField()
    class Meta:
        model = ProductInOrder
        fields = [
            'id',
            'product_variant',
            'order',
            'price',
            'quantity',
            'cost'
        ]
        read_only_fields = fields
