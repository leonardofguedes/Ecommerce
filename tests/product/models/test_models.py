from django.utils.text import slugify

from tests.product.base_test.test_base_product import *
from django.core.exceptions import ValidationError
from parameterized import parameterized


class ProductModelTeste(ProductTestBase):
    def setUp(self) -> None:
        self.product = self.make_product()
        return super().setUp()

    @parameterized.expand([
        ('title', 120),
        ('category', 25),
    ])
    def test_product_fields_max_lenght(self, field, max_lenght):
        setattr(self.product, field, 'A' * (max_lenght + 1))
        with self.assertRaises(ValidationError):
            self.product.full_clean()

    def test_product_string(self):
        needed = 'Representation Test'
        self.product.title = needed
        self.product.full_clean()
        self.product.save()
        self.assertEqual(str(self.product), needed)

    def test_slug_when_it_is_empty(self):
        slug = ''
        title = 'Test Title'
        id = 5000
        producttest = self.make_product(title=title, slug=slug, pk=id)
        slug_when_empty = f'{slugify(title)}'+f'{id}'
        self.assertEqual(slug_when_empty, producttest.slug)