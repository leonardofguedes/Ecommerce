from django.urls import path
from .views import *


urlpatterns = [
    path('', product_list_view, name='products'),
    path('<slug:slug>/', detail_view, name='detail')
]