import random
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import FormView, CreateView, ListView
from apps.core.models import Product
from .models import Order, Feedback, Cart, CartItem
from django import forms
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError

def get_or_create_cart(user):
    cart, _ =Cart.objects.get_or_create()
    return cart

def set_cart_item_quantity(user, product: Product, quantity: int):
    cart = get_or_create_cart(user=user)
    quantity = int(quantity)

    if quantity <= 0:
        CartItem.objects.filter(cart=cart, product=product).delete()
        return

    obj, _ = CartItem.objects.get_or_create(cart=cart, product=product)
    obj.quantity = quantity
    obj.save(update_fields=["quantity"])

def add_to_cart(user, obj: Product, quantity: int = 1) -> Order:
    
    cart = get_or_create_cart(user)
    obj, created = CartItem.objects.get_or_create(cart=cart, product=obj)

    if created:
        obj.quantity = max(1, int(quantity))
    else:
        obj.quantity = obj.quantity + max(1, int(quantity))

    obj.save(update_fields=["quantity"])
    return obj

def add_to_cart_view(request, slugify):
    product = get_object_or_404(Product, slugify=slugify)

    try:
        add_to_cart(request.user, product, quantity=1)
    except ValidationError:
        pass

    return redirect("user_feedback:cart")

def set_quantity_view(request, slugify):
    product = get_object_or_404(Product, slugify=slugify)
    qty = request.POST.get("quantity", "") or ""
    print(qty)

    if qty.isdigit() != True:
        return redirect("user_feedback:cart")

    try:
        set_cart_item_quantity(request.user, product, int(qty))
    except (ValueError, ValidationError):
        pass

    return redirect("user_feedback:cart")

class CartView(ListView):
    template_name = "user/cart.html"
    context_object_name = "item"
    paginate_by = 5
    model = CartItem

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["first_name", "last_name", "email", "phone", "adress", "message"]

class OrderView(CreateView):
    template_name = "user/order_form.html"
    form_class = OrderCreateForm
    success_url = "user:order"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("user:order")
    
class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["title", "name", "role", "message", "rating"]

class CommentView(CreateView):
    template_name = "user/comment.html"
    form_class = AddCommentForm
    success_url = reverse_lazy("core:home")