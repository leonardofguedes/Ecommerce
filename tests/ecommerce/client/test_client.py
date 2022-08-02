from django.test import TestCase
from django.urls import reverse


class EcommerceClientTest(TestCase):
    # status test
    def test_home_status(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_about_status(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_contact_status(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_login_status(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_status(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
    """
    
    path('logout/', logout_page, name='logout'),
    path('register/', register_page, name='register'),
    path('register/guest/', guest_register_view, name='guest_register'),
    path('api/cart/', cart_detail_api_view, name='api-cart'),
    path('cart/', cart, name='cart'),
    path('update/', cart_update, name='update'),
    path('checkout/', checkout_home, name='checkout'),
    path('checkout/address/create/', checkout_address_create_view, name='checkout_address_create'),
    path('checkout/address/reuse/', checkout_address_reuse_view, name='checkout_address_reuse'),
    path('checkout/success/', checkout_done_view, name='success'),
    """