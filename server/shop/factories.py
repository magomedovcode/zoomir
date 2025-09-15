from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from factory.django import DjangoModelFactory
import factory
from shop.models import ProductCategory, ProductChapter, Country, Brand, Product, ProductVariant

User = get_user_model()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    password = factory.PostGenerationMethodCall('set_password', 'password123')


class ProductChapterFactory(DjangoModelFactory):
    class Meta:
        model = ProductChapter

    name = factory.Sequence(lambda n: f"Товары для кошек {n}")


class ProductCategoryFactory(DjangoModelFactory):
    class Meta:
        model = ProductCategory

    name = factory.Sequence(lambda n: f"Сухой корм {n}")
    product_chapter = factory.SubFactory(ProductChapterFactory)


class CountryFactory(DjangoModelFactory):
    class Meta:
        model = Country

    name = factory.Sequence(lambda n: f"Страна производства {n}")
    flag = factory.LazyAttribute(
        lambda _: ContentFile(b"fake flag", "flag.png")
    )


class BrandFactory(DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Sequence(lambda n: f"Бренд производитель {n}")
    flag = factory.LazyAttribute(
        lambda _: ContentFile(b"fake logo", "logo.png")
    )


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Sequence(lambda n: f"Корм вискас {n}")
    description = factory.Sequence(lambda n: f"Очень вкусный корм {n}")
    product_category = factory.SubFactory(ProductCategoryFactory)
    country = factory.SubFactory(CountryFactory)
    brand = factory.SubFactory(BrandFactory)


class ProductVariantFactory(DjangoModelFactory):
    class Meta:
        model = ProductVariant

    name = factory.Sequence(lambda n: f"1 кг {n}")
    price = factory.Sequence(lambda n: f"1500 руб {n}")
    product = factory.SubFactory(ProductFactory)
