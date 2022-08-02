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
