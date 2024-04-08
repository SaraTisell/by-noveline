from django.views.generic import ListView
from django.shortcuts import render, redirect
from .models import WishList, WishListItem
from products.models import Product
from django.http import HttpResponseRedirect


class ViewWishList(ListView):
    model = WishListItem
    template_name = 'wishlist/wishlist.html'
    context_object_name = 'wishlist_items'

    def get_queryset(self):

        user_wishlist, created = WishList.objects.get_or_create(user=self.request.user)
        return user_wishlist.products.all()


def add_to_wishlist(request, product_id):
    product = Product.objects.get(id=product_id)
    user_wishlist = WishList.objects.get_or_create(user=request.user)[0]
    user_wishlist.products.add(product)
    return redirect('wishlist')