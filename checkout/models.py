import uuid
from django.db import models
from django.conf import settings
from django.db.models import Sum
from decimal import Decimal
from products.models import Product

class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    tax = models.DecimalField(max_digits=8, decimal_places=2, null=False, default=0)
    shipping_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=9)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):

        """ Using UUID to generate unique order number """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """ Update grand total based on line items """
        self.sub_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.shipping_cost = Decimal(settings.SHIPPING_COST)
        self.tax = self.sub_total * Decimal(settings.TAX_RATE)
        self.grand_total = self.sub_total + self.tax + self.shipping_cost
        self.save()

    def save(self, *args, **kwargs):
        """ Override default save method to set order number """
        if not self.order_number:
            self.order_number =self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=10)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """ Override dafault save method to set lineitem total and update sub total """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'

