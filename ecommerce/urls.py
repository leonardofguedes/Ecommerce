from django.urls import path
from .views import home_page, about, contact


urlpatterns = [
    path('', home_page),
    path('about/', about),
    path('contato/', contact),
]