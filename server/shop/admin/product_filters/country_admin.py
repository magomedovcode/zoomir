from django.contrib import admin
from nested_admin.nested import NestedModelAdmin
from shop.models import Country


@admin.register(Country)
class CountryAdmin(NestedModelAdmin):
    list_display = ('name', 'flag')
    search_fields = ('name', )
    ordering = ['name']
    list_per_page = 20

    fieldsets = (
        ('Заполните поля', {
            'fields': ('name', 'flag'),
        }),
    )
