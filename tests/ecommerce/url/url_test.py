from django.test import TestCase
from django.urls import reverse

class Urls(TestCase):
    def test_home_url(self):
        home_url = reverse('home')
        self.assertEqual(home_url, '/')

    def test_about_url(self):
        about_url = reverse('about')
        self.assertEqual(about_url, '/about/')

    def test_contact_url(self):
        contact_url = reverse('contact')
        self.assertEqual(contact_url, '/contato/')

    def test_login_url(self):
        login_url = reverse('login')
        self.assertEqual(login_url, '/login/')

    def test_logout_url(self):
        logout_url = reverse('logout')
        self.assertEqual(logout_url, '/logout/')

    def test_register_url(self):
        register_url = reverse('register')
        self.assertEqual(register_url, '/register/')

    def test_guest_register_url(self):
        guest_register_url = reverse('guest_register')
        self.assertEqual(guest_register_url, '/register/guest/')

    def test_api_cart_url(self):
        api_cart_url = reverse('api-cart')
        self.assertEqual(api_cart_url, '/api/cart/')

    def test_cart_url(self):
        cart_url = reverse('cart')
        self.assertEqual(cart_url, '/cart/')

    def update_url(self):
        update_url = reverse('update')
        self.assertEqual(update_url, '/update/')


    """
    
    
    path('checkout/', checkout_home, name='checkout'),
    path('checkout/address/create/', checkout_address_create_view, name='checkout_address_create'),
    path('checkout/address/reuse/', checkout_address_reuse_view, name='checkout_address_reuse'),
    path('checkout/success/', checkout_done_view, name='success'),
    """