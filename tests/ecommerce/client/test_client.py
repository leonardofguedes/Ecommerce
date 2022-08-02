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

    def test_register_status(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_guest_register_status(self):
        response = self.client.get(reverse('guest_register'))
        self.assertEqual(response.status_code, 302)

    def test_api_cart_status(self):
        response = self.client.get(reverse('api-cart'))
        self.assertEqual(response.status_code, 200)

    def test_cart_status(self):
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, 200)

    def test_update_status(self):
        response = self.client.get(reverse('update'))
        self.assertEqual(response.status_code, 302)

    def test_checkout_status(self):
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)

    def test_create_status(self):
        response = self.client.get(reverse('checkout_address_create'))
        self.assertEqual(response.status_code, 302)

    def test_checkout_sucess_status(self):
        response = self.client.get(reverse('success'))
        self.assertEqual(response.status_code, 200)

