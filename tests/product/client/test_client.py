from django.test import TestCase
from django.urls import reverse, resolve
from product.urls import *


class ProductClientTest(TestCase):
    def test_products_list_status(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)


"""
urlpatterns = [
    
    path('search/', search, name='search'),
    path('<slug:slug>/', detail_view, name='detail'),
]
"""