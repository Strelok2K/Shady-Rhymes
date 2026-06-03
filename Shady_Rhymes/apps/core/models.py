from django.db import models
from django.utils.text import slugify
from django.core.validators import MaxValueValidator
from decimal import Decimal

class Category(models.Model):
    name = models.CharField(max_length=100)
    slugify = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slugify:
            base = slugify(self.name)[:100] or 'category'
            candidate_slug = base
            i = 1
            while Category.objects.filter(slugify=candidate_slug).exists():
                candidate_slug = f'{base}{i}'
                i += 1
            self.slugify = candidate_slug

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(Decimal("10"))])
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slugify = models.SlugField(unique=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slugify:
            base = slugify(self.name)[:100] or 'product'
            candidate_slug = base
            i = 1
            while Product.objects.filter(slugify=candidate_slug).exists():
                candidate_slug = f'{base}{i}'
                i += 1
            self.slugify = candidate_slug

        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.name}'