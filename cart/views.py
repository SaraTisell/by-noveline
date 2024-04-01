from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView
from django.contrib import messages


class ViewShoppingCart(TemplateView):
    """ View to render cart """

    template_name = 'cart/cart.html'

def add_to_cart(request, item_id):
    """ Function to add item to cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('selected_size')
    size2 = request.POST.get ('selected_size_ring_set')
    cart = request.session.get('cart', {})

    cart_key = f"{item_id}-{size}-{size2}" if size2 else f"{item_id}-{size}"

    if cart_key not in cart:
        cart[cart_key] = {
            'item_id': item_id,
            'size': size,
            'size2': size2,
            'quantity': 0,
        }
    
    cart[cart_key]['quantity'] += quantity
    messages.success(request, "Added product to cart")

    request.session['cart'] = cart
    return redirect(redirect_url)

def adjust_cart(request, cart_key):
    """ Function to adjust quantity for a item in the cart """

    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity'))

    if cart_key in cart:
        if quantity > 0:
            cart[cart_key]['quantity'] = quantity
            messages.success(request, "Updated product quantity")
        else:
            del cart[cart_key]
            messages.success(request, "Removed product from cart")

    request.session['cart'] = cart
    return redirect(reverse('cart'))

def remove_from_cart(request, cart_key):
    """ Function to remove a item from the cart """

    cart = request.session.get('cart', {})

    if cart_key in cart:
        del cart[cart_key]
        
    request.session['cart'] = cart
    return redirect(reverse('cart'))
