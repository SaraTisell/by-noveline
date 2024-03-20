from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Category, Product

class AllProducts(ListView):
    """ View to display all products """

    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'


class SearchResultsView(ListView):
    """ View to display products based on search queries """
    model = Product
    template_name = 'products/search_results.html'

    # Function to sort products based on serach term in name or description
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        return object_list

    # Get search term from form to use dynamic in template
    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context['search_term'] = self.request.GET.get('q')

        return context

class ProductDetail(DetailView):
    """ View for each individual product details """
    model = Product
    template_name = 'products/product_detail.html'
    slug_field = 'slug'