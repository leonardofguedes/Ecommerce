from django.urls import path
from .views import *


urlpatterns = [
    path('', home_page),
    path('about/', about),
    path('contato/', contact),
    path('login/', login_view),
    path('register/', register_page)
]