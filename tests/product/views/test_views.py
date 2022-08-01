from django.test import TestCase
from django.urls import reverse, resolve
from product.urls import *


class ProductViewTest(TestCase):
    def test_products_list_view(self):
        view = resolve(reverse('products'))
        self.assertIs(view.func, product_list_view)

    def test_search_view(self):
        view = resolve(reverse('search'))
        self.assertIs(view.func, search)

    def test_detail_view(self):
        view = resolve(reverse('detail', kwargs={'slug': 'teste-teste'}))
        self.assertIs(view.func, detail_view)
