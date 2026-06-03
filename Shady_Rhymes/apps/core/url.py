from django.urls import path
from .views import(
    HomeView,
    ProductView,
    ProductDetailView
)

app_name = "core"

urlpatterns =[
    path("", HomeView.as_view(), name='home'),
    path("products/", ProductView.as_view(), name="product"),
    path("product/<slug:slugify>", ProductDetailView.as_view(), name="product_detail")
]