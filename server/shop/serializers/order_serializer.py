from shop.models import Order, ProductInOrder, ProductVariant
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from .product_in_order_serializer import ProductInOrderSerializer


@extend_schema_serializer(component_name='Order')
class OrderSerializer(serializers.ModelSerializer):
    products_in_orders = ProductInOrderSerializer(
        many=True,
        read_only=True
    )
    user = serializers.StringRelatedField(
        read_only=True
    )
    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'address',
            'phone',
            'delivery_date',
            'date',
            'status',
            'products_in_orders'
        ]
        read_only_fields = fields


@extend_schema_serializer(component_name='OrderCreate')
class OrderCreateSerializer(serializers.ModelSerializer):
    products = serializers.ListField(
        child=serializers.DictField(),
        write_only=True,
        help_text=_('Список товаров в формате [{"product_variant": id, "quantity": number}]')
    )
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Order
        fields = [
            'user',
            'address',
            'phone',
            'delivery_date',
            'products'
        ]

    @staticmethod
    def validate_products(value):
        if not value:
            raise serializers.ValidationError(_('Заказ должен содержать хотя бы один товар'))

        for product in value:
            if 'product_variant' not in product or 'quantity' not in product:
                raise serializers.ValidationError(_('Каждый товар должен содержать product_variant и quantity'))

            if product['quantity'] < 1:
                raise serializers.ValidationError(_('Количество товара должно быть не менее 1'))

        return value

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        order = Order.objects.create(**validated_data)

        for product_data in products_data:
            product_variant = ProductVariant.objects.get(id=product_data['product_variant'])
            ProductInOrder.objects.create(
                order=order,
                product_variant=product_variant,
                price=product_variant.price,
                quantity=product_data['quantity']
            )

        return order


@extend_schema_serializer(component_name='OrderStatusUpdate')
class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']
