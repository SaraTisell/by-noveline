from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "You have nothing in your cart yet")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51P1QzoDmTB5DF9hE1quFMg9XAb65GpfbSHjuKJtJXPhzLARXJLxR8mq6D692jliqAUmLQkbQlvDZwa2rVIJUd1lh00KcOyfq6d',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)