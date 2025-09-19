from shop.models import Cart
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from shop.serializers.cart_content.product_in_cart_serializer import ProductInCartSerializer


@extend_schema_serializer(component_name='Cart')
class CartSerializer(serializers.ModelSerializer):
    products_in_carts = ProductInCartSerializer(
        many=True,
        read_only=True
    )
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
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
