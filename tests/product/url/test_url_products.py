from django.test import TestCase
from django.urls import reverse


class ProductUrls(TestCase):
    def test_products_list_url(self):
        product_url = reverse('products')
        self.assertEqual(product_url, '/produtos/')

    def test_search_url(self):
        search_url = reverse('search')
        self.assertEqual(search_url, '/produtos/search/')

    def test_detail_url(self):
        detail_url = reverse('detail', kwargs={'slug': 'teste-slug'})
        self.assertEqual(detail_url, '/produtos/teste-slug/')
