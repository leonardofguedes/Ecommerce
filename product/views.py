from django.db.models import Q
from django.http import Http404
from django.views.generic import ListView
from .models import Product
from django.shortcuts import render
from .models import Product


def product_list_view(request):
    products = Product.objects.all()
    context = {
        'products': products,
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

def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    products = Product.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term) |
            Q(category__icontains=search_term),
        ))
    return render(request, 'pages/search.html', {
        'search_term': search_term,
        'products': products,
    })

