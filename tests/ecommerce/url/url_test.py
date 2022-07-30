from django.test import TestCase
from django.urls import reverse

class Urls(TestCase):
    def test_home_url_is_correct(self):
        home_url = reverse('home')
        self.assertEqual(home_url, '/')