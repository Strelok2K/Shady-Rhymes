from apps.core.models import Product

def get_product_query(q: str | None):
    qs = (
        Product.objects.filter(is_active = True)
    )

    if q:
        qs = qs.filter(
            name=q.capitalize()
        )

    return qs.order_by("-created_at")