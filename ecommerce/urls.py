from django.urls import path
from ecommerce.views.about import *
from ecommerce.views.contact import *
from ecommerce.views.home_page import *
from ecommerce.views.login import *
from ecommerce.views.logout import *
from ecommerce.views.register import *


urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about, name='about'),
    path('contato/', contact, name='contact'),
    path('login/', login_view, name='login'),
    path('logout/', logout_page, name='logout'),
    path('register/', register_page, name='register'),
]