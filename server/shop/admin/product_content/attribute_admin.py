from django.contrib import admin
from nested_admin.nested import NestedModelAdmin
from shop.models import Attribute


@admin.register(Attribute)
class AttributeAdmin(NestedModelAdmin):
    list_display = ('name', 'value', 'product_variant', 'attribute_category')
    list_filter = ('product_variant', 'attribute_category')
    search_fields = ('name', 'product_variant__name')
    ordering = ['-id']
    autocomplete_fields = ['product_variant', 'attribute_category']
    list_per_page = 20

    fieldsets = (
        ('Выберите параметры', {
            'fields': ('product_variant', 'attribute_category')
        }),
        ('Заполните поля', {
            'fields': ('name', 'value'),
        }),
    )
