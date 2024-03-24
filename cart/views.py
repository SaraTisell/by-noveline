from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class ViewShoppingCart(TemplateView):

    template_name = 'cart/cart.html'


def add_to_cart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('selected_size')
    size2 = None
    if 'selected_size_ring_set' in request.POST:
        size2 = request.POST['selected_size_ring_set']
    cart = request.session.get('cart', {})


    if item_id not in cart:
        cart[item_id] = {}

        if size in cart[item_id]:
            cart[item_id][size] += quantity
        else:
            cart[item_id][size] = quantity
    else:
        cart[item_id] = {size: quantity}
    
        if size2:
            if item_id in cart:
                cart[item_id]['size2'] = size2
            else:
                cart[item_id] = {size: quantity, 'size2': size2}


    request.session['cart'] = cart
    return redirect(redirect_url)