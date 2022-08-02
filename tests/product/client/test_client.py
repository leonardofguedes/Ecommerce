from django.urls import reverse
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
    def test_products_list_with_product(self):
        product = self.make_product()
        list_url = reverse('products')
        response = self.client.get(list_url)
        self.assertIn(product, response.context['products'])

    def test_products_list_content(self):
        title = 'Produto Amarelo'
        product = self.make_product(title=title)
        response = self.client.get(reverse('products'))
        content = response.content.decode('utf-8')
        self.assertIn(title, content)

    def test_search_with_product(self):
        product = self.make_product()
        search_url = reverse('search')
        response1 = self.client.get(f'{search_url}?q=produto-teste')
        self.assertIn(product, response1.context['products'])

    def test_search_with_specific_product_title(self):
        product = self.make_product(title='produto deteriorado')
        search_url = reverse('search')
        response1 = self.client.get(f'{search_url}?q=deteriorado')
        self.assertIn(product, response1.context['products'])

    def test_search_with_two_products_made(self):
        title1 = 'produto deteriorado'
        slug1 = 'slug-teste-1'
        title2 = 'produto amarelo'
        slug2 = 'slug-teste-2'
        product1 = self.make_product(title=title1, slug=slug1)
        product2 = self.make_product(title=title2, slug=slug2)
        search_url = reverse('search')
        response1 = self.client.get(f'{search_url}?q={title1}')
        response2 = self.client.get(f'{search_url}?q={title2}')
        response3 = self.client.get(f'{search_url}?q=produto')
        self.assertIn(product1, response1.context['products'])
        self.assertIn(product2, response2.context['products'])
        self.assertIn(product2, response3.context['products'])

    def test_search_with_search_term_wrong(self):
        product = self.make_product()
        mensagem = 'O produto não foi encontrado'
        search_url = reverse('search')
        response1 = self.client.get(f'{search_url}?q=amarelo')
        content = response1.content.decode('utf-8')
        self.assertIn(mensagem, content)