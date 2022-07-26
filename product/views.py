from django.http import Http404
from django.shortcuts import render
from .models import Product


def product_list_view(request):
    products = Product.objects.all()
    context = {
        'produtos': products,
        'title': 'PROVISÓRIO1'
    }
    return render(request, "pages/products_list.html", context)

def detail_view(request, slug):
    product = Product.objects.filter(slug__iexact=slug).first()
    if not product:
        return render(request, "pages/detail.html", context={
            'product': f'O produto não foi encontrado'
        })
    else:
        return render(request, "pages/detail.html", context={
            'product': product,
            'title': 'PROVISÓRIO2',
        })