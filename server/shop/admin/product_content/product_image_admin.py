from django.contrib import admin
from nested_admin.nested import NestedModelAdmin
from shop.models import ProductImage


@admin.register(ProductImage)
class ProductImageAdmin(NestedModelAdmin):
    list_display = ('product_variant', 'image')
    list_filter = ('product_variant', )
    ordering = ['id']
    autocomplete_fields = ['product_variant']
    list_per_page = 20

    fieldsets = (
        ('Выберите параметры', {
            'fields': ('product_variant', )
        }),
        ('Заполните поля', {
            'fields': ('image', ),
        }),
    )
