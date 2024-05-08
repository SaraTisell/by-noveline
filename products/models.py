from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
         'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    sku = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.BooleanField(default=True)
    size_ring_sets = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
