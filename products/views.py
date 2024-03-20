from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from .models import Category, Product
from .forms import AdminAddProductForm

class AllProducts(ListView):
    """ View to display all products """
    """ View to sort products based on category"""

    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'

    # Function to retrieve products based on selected category from nav link
    def get_queryset(self):
        category_name = self.request.GET.get('category')
        if category_name:
            return Product.objects.filter(category__name=category_name)
        else:
            return Product.objects.all()

    # Get category_name to use in template
    def get_context_data(self, **kwargs):
        context = super(AllProducts, self).get_context_data(**kwargs)
        context['category_name'] = self.request.GET.get('category')

        return context

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

class AddNewProduct(UserPassesTestMixin, CreateView):
    """ View to render AdminAddProductForm """

    template_name = 'products/add_product.html'
    form_class = AdminAddProductForm
    success_url = reverse_lazy('add_product')

    def test_func(self):
        """ Test user is superuser """
        return self.request.user.is_superuser





