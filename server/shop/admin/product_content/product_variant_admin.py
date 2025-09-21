from django.contrib import admin
from nested_admin.nested import NestedModelAdmin
from shop.models import ProductVariant
from shop.admin.inlines import (
    AttributeInline,
    ProductImageInline
)


@admin.register(ProductVariant)
class ProductVariantAdmin(NestedModelAdmin):
    list_display = ('name', 'price', 'product')
    list_filter = ('product', )
    search_fields = ('name', 'product__title')
    ordering = ['-id']
    autocomplete_fields = ['product']
    inlines = [AttributeInline, ProductImageInline]
    list_per_page = 20

    fieldsets = (
        ('Выберите параметры', {
            'fields': ('product', )
        }),
        ('Заполните поля', {
            'fields': ('name', 'price'),
        }),
    )
