from django.urls import path
from .views import(
    CartView,
    add_to_cart_view,
    set_quantity_view,
    CommentView
)

app_name = "user_feedback"

urlpatterns = [
    path("cart/", CartView.as_view(), name="cart"),
    path("cart/add/<slug:slugify>/", add_to_cart_view, name="add_to_cart"),
    path("cart/qty/<slug:slugify>/", set_quantity_view, name="set_qty"),
    path("comment/", CommentView.as_view(), name="comment")
]