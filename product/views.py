from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Product


def product_list_view(request):
    products = Product.objects.all()
    context = {
        'produtos': products
    }
    return render(request, "pages/products_list.html", context)

def detail_view(request, id):
    product = Product.objects.filter(id=id).first()
    if not product:
        return render(request, "pages/detail.html", context={
            'product': f'O produto com id {id} não existe'
        })
    else:
        return render(request, "pages/detail.html", context={
            'product': product
        })