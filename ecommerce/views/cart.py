from django.shortcuts import render, redirect
from product.models import Product
from ecommerce.models.cart_models import Cart
from ecommerce.models.orders_models import Order
from ecommerce.models.billing_models import BillingProfile
from ecommerce.forms.login_form import LoginForm
from ecommerce.forms.account_form import GuestForm
from ecommerce.models.account_models import GuestEmail


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

def checkout_home(request):
    #aqui a gente pega o carrinho
    cart_obj, cart_created= Cart.objects.new_or_get(request)
    order_obj = None
    #se o carrinho acabou de ser criado, ele tá zerado
    #ou se o carrinho já existir mas não tiver nada dentro
    if cart_created or cart_obj.products.count() == 0:
        return redirect("cart")
    #aqui a order associada ao carrinho
    else:
        order_obj, new_order_obj = Order.objects.get_or_create(cart = cart_obj)
    user = request.user
    billing_profile = None
    login_form = LoginForm()
    guest_form = GuestForm()
    guest_email_id = request.session.get('guest_email_id')
    if user.is_authenticated:
        billing_profile, billing_profile_created = BillingProfile.objects.get_or_create(user=user, email=user.email)
    elif guest_email_id is not None:
        guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
        billing_profile, billing_guest_profile_created = BillingProfile.objects.get_or_create(
    email=guest_email_obj.email)
    else:
        pass
    if billing_profile is not None:
        order_qs = Order.objects.filter(billing_profile=billing_profile, cart=cart_obj, active=True)
        if order_qs.count() == 1:
            order_obj = order_qs.first()
        else:
            old_order_qs = Order.objects.exclude(billing_profile=billing_profile).filter(cart=cart_obj, active=True)
            if old_order_qs.exists():
                old_order_qs.update(active=False)
            order_obj = Order.objects.create(billing_profile=billing_profile, cart=cart_obj)
    context = {
        "object": order_obj,
        "billing_profile": billing_profile,
        "login_form ": login_form,
        "guest_form": guest_form,
    }
    return render(request, "pages/checkout.html", context)