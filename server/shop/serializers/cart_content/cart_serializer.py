from shop.models import Cart
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from shop.serializers import ProductInCartSerializer


@extend_schema_serializer(component_name='Cart')
class CartSerializer(serializers.ModelSerializer):
    products_in_carts = ProductInCartSerializer(
        many=True,
        read_only=True
    )
    user = serializers.StringRelatedField(
        read_only=True
    )
    class Meta:
        model = Cart
        fields = [
            'id',
            'user',
            'date',
            'products_in_carts'
        ]
        read_only_fields = fields
