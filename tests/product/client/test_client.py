from django.test import TestCase
from django.urls import reverse, resolve
from tests.product.base_test.test_base_product import *


class ProductClientTest(ProductTestBase):
    # status test
    def test_products_list_status(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)

    def test_search_status_with_no_product_registered(self):
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 404)

    def test_detail_status_with_no_product_registered(self):
        response = self.client.get(reverse('detail', kwargs={'slug': 'teste'}))
        self.assertEqual(response.status_code, 200)
    # template test
    def test_products_list_template(self):
        response = self.client.get(reverse('products'))
        self.assertTemplateUsed(response, 'pages/products_list.html')

    def test_detail_template(self):
        response = self.client.get(reverse('detail', kwargs={'slug': 'teste-slug'}))
        self.assertTemplateUsed(response, 'pages/detail.html')

    def test_search_template(self):
        response = self.client.get(reverse('search') + '?q=teste')
        self.assertTemplateUsed(response, 'pages/search.html')

    # product made test
    def test_search_with_product(self):
        product = self.make_product()
        search_url = reverse('search')
        response1 = self.client.get(f'{search_url}?q=produto-teste')
        self.assertIn(product, response1.context['products'])
