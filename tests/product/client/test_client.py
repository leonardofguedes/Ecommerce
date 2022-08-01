from django.test import TestCase
from django.urls import reverse, resolve
from product.urls import *


class ProductClientTest(TestCase):
    def test_products_list_status(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)

    def test_search_status_with_no_product_registered(self):
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 404)

    def test_detail_with_no_product_registered(self):
        response = self.client.get(reverse('detail', kwargs={'slug': 'teste'}))
        self.assertEqual(response.status_code, 200)

    def test_products_list_template(self):
        response = self.client.get(reverse('products'))
        self.assertTemplateUsed(response, 'pages/products_list.html')
