from shop.models import ProductInCart, Cart
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from .product_variant_serializer import ProductVariantSerializer


@extend_schema_serializer(component_name='ProductInCart')
class ProductInCartSerializer(serializers.ModelSerializer):
    product_variant = ProductVariantSerializer(
        read_only=True
    )
    class Meta:
        model = ProductInCart
        fields = [
            'id',
            'product_variant',
            'quantity'
        ]
        read_only_fields = fields


@extend_schema_serializer(component_name='ProductInCartCreate')
class ProductInCartCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = ProductInCart
        fields = [
            'product_variant',
            'quantity'
        ]

    def create(self, validated_data):
        cart, created = Cart.objects.get_or_create(user=validated_data['user'])
        validated_data['cart'] = cart

        product_in_cart, created = ProductInCart.objects.get_or_create(
            cart=cart,
            product_variant=validated_data['product_variant'],
            defaults={'quantity': validated_data['quantity']}
        )

        if not created:
            product_in_cart.quantity += validated_data['quantity']
            product_in_cart.save()

        return product_in_cart
