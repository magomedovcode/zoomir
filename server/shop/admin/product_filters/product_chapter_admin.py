from django.contrib import admin
from nested_admin.nested import NestedModelAdmin
from shop.models import ProductChapter


@admin.register(ProductChapter)
class ProductChapterAdmin(NestedModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    ordering = ['name']
    list_per_page = 20

    fieldsets = (
        ('Заполните поля', {
            'fields': ('name',),
        }),
    )
