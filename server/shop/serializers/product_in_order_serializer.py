from shop.models import ProductInOrder
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers

from shop.serializers.product_variant_serializer import ProductVariantSerializer


@extend_schema_serializer(component_name='ProductInOrder')
class ProductInOrderSerializer(serializers.ModelSerializer):
    product_variant = ProductVariantSerializer(
        read_only=True
    )
    cost = serializers.ReadOnlyField()
    class Meta:
        model = ProductInOrder
        fields = [
            'id',
            'product_variant',
            'price',
            'quantity',
            'cost'
        ]
        read_only_fields = fields
