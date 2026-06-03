import random
from django.views.generic import TemplateView, ListView, DetailView
from .models import Product, Category
from apps.user_feedback.models import Feedback

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        qs = Product.objects.filter(
            Product.is_active == True
        )

        ids = list(qs.values_list("id", flat=True)[:200])
        random_ids = random.sample(ids, min(len(ids), 4)) if ids else []
        random_obj = list(
            Product.objects.filter(ids__in=random_ids)
        )

        random_obj.sort(key=lambda x: random_ids.index(x.id))

        ctx["random_obj"] = random_obj

        return ctx
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        qs = Product.objects.all()

        ids1 = list(qs.values_list("id", flat=True)[:200])
        random_ids = random.sample(ids1, min(len(ids1), 4)) if ids1 else []
        random_obj = list(
            Product.objects.filter(id__in=random_ids)
        )

        random_obj.sort(key=lambda x: random_ids.index(x.id))
    
        ctx = super().get_context_data(**kwargs)
        qs = Category.objects.all()

        ids2 = list(qs.values_list("id", flat=True)[:200])
        random_ids2 = random.sample(ids2, min(len(ids2), 4)) if ids2 else []
        random_cat = list(
            Category.objects.filter(id__in=random_ids2)
        )

        random_cat.sort(key=lambda x: random_ids2.index(x.id))

        ctx = super().get_context_data(**kwargs)
        qs = Feedback.objects.all()

        ids3 = list(qs.values_list("id", flat=True)[:200])
        random_ids3 = random.sample(ids3, min(len(ids3), 3)) if ids3 else []
        random_com = list(
            Feedback.objects.filter(id__in=random_ids3)
        )

        random_com.sort(key=lambda x: random_ids3.index(x.id))

        ctx["random_com"] = random_com
        ctx["random_cat"] = random_cat
        ctx["random_obj"] = random_obj

        return ctx

class ProductView(ListView):
    template_name = 'core/products.html'
    context_object_name = 'product'
    paginate_by = 12

    def get_queryset(self):
        return Product.objects.all()

class ProductDetailView(DetailView):
    template_name = 'core/detail.html'
    model = Product
    slug_field = "slugify"
    slug_url_kwarg = "slugify"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        qs = Product.objects.all()

        ids = list(qs.values_list("id", flat=True)[:200])
        random_ids = random.sample(ids, min(len(ids), 3)) if ids else []
        random_obj = list(
            Product.objects.filter(id__in=random_ids)
        )

        random_obj.sort(key=lambda x: random_ids.index(x.id))

        ctx["random_obj"] = random_obj

        return ctx