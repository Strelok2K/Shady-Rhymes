from django.contrib import admin
from .models import(
    Order,
    Cart,
    CartItem,
    Feedback
)

admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Feedback)