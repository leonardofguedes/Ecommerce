from django.urls import path
from .views import *


urlpatterns = [
    path('', product_list_view),
    path('<int:pk>', detail_view)
]