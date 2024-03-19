from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, Product

class AllProducts(ListView):

    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'


