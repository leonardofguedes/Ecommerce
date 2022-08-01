from django.test import TestCase
from django.urls import reverse, resolve
from product.urls import *


class ProductViewTest(TestCase):
    def test_products_list_view(self):
        view = resolve(reverse('products'))
        self.assertIs(view.func, product_list_view)


urlpatterns = [
    path('search/', search, name='search'),
    path('<slug:slug>/', detail_view, name='detail'),
]