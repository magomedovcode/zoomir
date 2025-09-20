from django.contrib import admin
from nested_admin.nested import NestedModelAdmin
from shop.models import ProductInCart


@admin.register(ProductInCart)
class ProductInCartAdmin(NestedModelAdmin):
    list_display = ('cart', 'product_variant', 'quantity')
    list_filter = ('cart', 'product_variant')
    search_fields = ('cart__user__username', 'product_variant__name')
    ordering = ['-id']
    autocomplete_fields = ['cart', 'product_variant']
    list_per_page = 20

    fieldsets = (
        ('Выберите параметры', {
            'fields': ('cart', 'product_variant')
        }),
        ('Заполните поля', {
            'fields': ('quantity',),
        }),
    )
