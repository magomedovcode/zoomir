from drf_spectacular.utils import extend_schema
from shop.serializers import OrderCreateSerializer
from rest_framework import (
    permissions,
    generics
)
from shop.models import (
    Order,
    UserTag
)


@extend_schema(tags=['Заказы'], request=OrderCreateSerializer)
class OrderCreateView(generics.CreateAPIView):
    """
    Создание нового заказа
    """
    serializer_class = OrderCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        order = serializer.save(user=self.request.user)
        self._update_user_tag_preferences(order)
        order.user.cart.products_in_carts.all().delete()

    @staticmethod
    def _update_user_tag_preferences(order: Order):
        """
        Увеличивает вес тегов у пользователя на основании товаров в заказе
        """
        for item in order.products_in_orders.select_related("product_variant").all():
            product_variant = item.product_variant
            for tag in product_variant.tags.all():
                pref, _ = UserTag.objects.get_or_create(
                    user=order.user,
                    tag=tag,
                    defaults={"weight": 0}
                )
                pref.weight += 1
                pref.save()
