from django.test import TestCase
from django.urls import reverse, resolve
from ecommerce.urls import *


class EcommerceViewTest(TestCase):
    def test_homepage_view(self):
        view = resolve(reverse('home'))
        self.assertIs(view.func, home_page )

    def test_about_view(self):
        view = resolve(reverse('about'))
        self.assertIs(view.func, about)

    def test_contato_view(self):
        view = resolve(reverse('contact'))
        self.assertIs(view.func, contact)


"""
urlpatterns = [
    path('login/', login_view, name='login'),
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
]
"""