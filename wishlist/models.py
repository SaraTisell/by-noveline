from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.user.username}'s Wishlist"


class WishListItem(models.Model):
    product = models.ForeignKey(
            Product, null=False, blank=False, on_delete=models.CASCADE)
    wishlist = models.ForeignKey(
            WishList, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
