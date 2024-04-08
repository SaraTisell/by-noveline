from django.views.generic import ListView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import WishList, WishListItem
from django.contrib import messages
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
    redirect_url = request.POST.get('redirect_url')
    product = Product.objects.get(id=product_id)
    user_wishlist = WishList.objects.get_or_create(user=request.user)[0]
    user_wishlist.products.add(product)

    messages.success(request, f"{product.name} has been added to your wishlist 🩷.")
    return redirect(redirect_url)

class RemoveItemFromWishList(DeleteView):
    model = WishListItem
    template_name = 'wishlist/remove_item_confirm.html'
    success_url = reverse_lazy('home')