from django.shortcuts import render
from django.views.generic import ListView
from .models import Product


def product_list_view(request):
    products = Product.objects.all()
    context = {
        'produtos': products
    }
    return render(request, "pages/products_list.html", context)
