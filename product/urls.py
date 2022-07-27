from django.urls import path
from .views import *


urlpatterns = [
    path('', product_list_view, name='products'),
    path('search/', search, name='search'),
    path('<slug:slug>/', detail_view, name='detail'),
]