from django.contrib import admin
from nested_admin.nested import NestedModelAdmin
from shop.models import AttributeCategory


@admin.register(AttributeCategory)
class AttributeCategoryAdmin(NestedModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    ordering = ['name']
    list_per_page = 20

    fieldsets = (
        ('Заполните поля', {
            'fields': ('name', ),
        }),
    )
