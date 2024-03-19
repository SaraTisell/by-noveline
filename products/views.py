from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Product

class AllProducts(ListView):

    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'

class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    slug_field = 'slug'