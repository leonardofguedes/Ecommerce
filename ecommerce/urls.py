from django.urls import path
from ecommerce.views.about import *
from ecommerce.views.contact import *
from ecommerce.views.home_page import *
from ecommerce.views.login import *
from ecommerce.views.logout import *
from ecommerce.views.register import *
from ecommerce.views.cart import *
from ecommerce.views.addresses import *


urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about, name='about'),
    path('contato/', contact, name='contact'),
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