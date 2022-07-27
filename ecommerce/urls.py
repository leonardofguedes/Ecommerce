from django.urls import path
from .views import *


urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about),
    path('contato/', contact, name='contact'),
    path('login/', login_view, name='login'),
    path('logout/', logout_page, name='logout'),
    path('register/', register_page, name='register'),
]