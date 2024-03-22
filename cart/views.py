from django.shortcuts import render
from django.views.generic import TemplateView

class ViewShoppingCart(TemplateView):

    template_name = 'cart/cart.html'

