from django.shortcuts import render, redirect
from django.views.generic import TemplateView


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

    request.session['cart'] = cart
    return redirect(redirect_url)

def adjust_cart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('selected_size')
    size2 = request.POST.get ('selected_size_ring_set')
    cart = request.session.get('cart', {})

    cart_key = f"{item_id}-{size}-{size2}" if size2 else f"{item_id}-{size}"

    if cart_key in cart:
        cart[cart_key] = quantity

    request.session['cart'] = cart
    return redirect('cart')