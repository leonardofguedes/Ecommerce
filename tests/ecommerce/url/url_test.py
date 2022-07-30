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