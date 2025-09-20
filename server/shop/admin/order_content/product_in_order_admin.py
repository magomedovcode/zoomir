from django.contrib import admin
from nested_admin.nested import NestedModelAdmin
from shop.models import ProductInOrder


@admin.register(ProductInOrder)
class ProductInOrderAdmin(NestedModelAdmin):
    list_display = ('order', 'product_variant', 'price', 'quantity')
    list_filter = ('order', 'product_variant')
    ordering = ['id']
    autocomplete_fields = ['order', 'product_variant']
    list_per_page = 20

    fieldsets = (
        ('Выберите параметры', {
            'fields': ('order', 'product_variant')
        }),
        ('Заполните поля', {
            'fields': ('price', 'quantity'),
        }),
    )
