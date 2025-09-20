from django.contrib import admin
from nested_admin.nested import NestedModelAdmin
from shop.models import Brand


@admin.register(Brand)
class BrandAdmin(NestedModelAdmin):
    list_display = ('name', 'logo')
    search_fields = ('name', )
    ordering = ['name']
    list_per_page = 20

    fieldsets = (
        ('Заполните поля', {
            'fields': ('name', 'logo'),
        }),
    )
