from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Product


def product_list_view(request):
    products = Product.objects.all()
    context = {
        'produtos': products
    }
    return render(request, "pages/products_list.html", context)

def detail_view(request, pk=id):
    product = get_object_or_404(Product, pk = pk)
    context = {
        'product': product
    }
    return render(request, "pages/detail.html", context)