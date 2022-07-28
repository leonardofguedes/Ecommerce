from django.shortcuts import render, redirect
from product.models import Product
from ecommerce.models import Cart


def cart(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "pages/cart.html", {"cart": cart_obj})


def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Mostra mensagem para o usuário, produto em falta?")
            return redirect("cart")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)  # cart_obj.products.add(product_id)
        request.session['cart_items']=cart_obj.products.count()
    return redirect("cart")