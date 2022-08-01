from django.test import TestCase
from product.models import Product


class ProductMixin:
    def make_product(self,
                     title = 'produto-teste',
                     category = 'Livros',
                     description = 'Descrição Teste',
                     price = 100,
                     slug='Product-Slug-Test'
                     ):
        return Product.objects.create(
            title=title,
            category=category,
            description=description,
            price=price,
            slug=slug,
        )

    def make_more_products(self, qtd=10):
        products = []
        for h in range(qtd):
            kwargs = {
                'title': f'Product Title {h}',
                'slug':f'Product{h}',
            }
            product = self.make_product(**kwargs)
            products.append(product)
        return products


class ProductTestBase(TestCase, ProductMixin):
    def setUp(self) -> None:
        return super().setUp()