from django.urls import path
from . import views

urlpatterns = [
    path(
        'product-chapters-list/',
        views.ProductChapterListView.as_view(),
        name='product-chapters-list'
    ),
    path(
        'product-categories-list/',
        views.ProductCategoryListView.as_view(),
        name='product-categories-list'
    ),
    path(
        'brand-list/',
        views.BrandListView.as_view(),
        name='brand-list'
    ),
    path(
        'country-list/',
        views.CountryListView.as_view(),
        name='country-list'
    ),
    path(
        'product-list/',
        views.ProductListView.as_view(),
        name='product-list'
    ),
    path(
        'attribute-categories-list/',
        views.AttributeCategoryListView.as_view(),
        name='attribute-categories-list'
    )
]
