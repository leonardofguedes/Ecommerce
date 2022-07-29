from django.contrib import admin
from .models.cart_models import Cart
from .models.orders_models import Order
from .models.billing_models import BillingProfile
from .models.account_models import GuestEmail
from .models.addresses_models import Address


admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(BillingProfile)
admin.site.register(GuestEmail)
admin.site.register(Address)