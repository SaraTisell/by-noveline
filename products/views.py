from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
    )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Category, Product
from .forms import AdminAddProductForm


class AllProducts(ListView):
    """
        View to display all products
        View to sort products based on category
    """

    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'

    def get_queryset(self):
        """ Function to retrieve products based on
        selected category from nav link
        """
        category_name = self.request.GET.get('category')
        if category_name:
            return Product.objects.filter(category__name=category_name)
        else:
            return Product.objects.all()

    def get_context_data(self, **kwargs):
        """ Get category_name to use in template """
        context = super(AllProducts, self).get_context_data(**kwargs)
        context['category_name'] = self.request.GET.get('category')

        return context


class SearchResultsView(ListView):
    """ View to display products based on search queries """
    model = Product
    template_name = 'products/search_results.html'

    def get_queryset(self):
        """ Function to sort products based on serach term
        in name or description
        """
        query = self.request.GET.get("q")
        object_list = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        return object_list

    def get_context_data(self, **kwargs):
        """ Get search term from form to use dynamic in template """
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context['search_term'] = self.request.GET.get('q')

        return context


class ProductDetail(DetailView):
    """ View for each individual product details """
    model = Product
    template_name = 'products/product_detail.html'
    slug_field = 'slug'


class AddNewProduct(UserPassesTestMixin, CreateView):
    """
        View for admin to add new product
        And list all existing products
    """
    model = Product
    template_name = 'products/manage_products.html'
    form_class = AdminAddProductForm
    success_url = reverse_lazy('manage_products')

    def test_func(self):
        """ Test user is superuser """
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all().order_by('category')

        return context

    def form_valid(self, form):
        """ Test if form is valid
            Saves product name to use in message if form is valid
        """
        product = form.save(commit=False)
        product_name = form.cleaned_data['name']

        form.save()
        messages.success(self.request, f"New Product {product_name} added")
        return super().form_valid(form)

    def form_invalid(self, form):
        """ If form is not valid an error message is displayed """
        messages.error = (
            self.request, "FAILED TO ADD PRODUCT - ensure all field is valid")
        return super().form_invalid(form)


class UpdateProduct(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """ View to update an existing product """
    model = Product
    form_class = AdminAddProductForm
    template_name = 'products/update_product.html'
    success_url = reverse_lazy('manage_products')
    success_message = "Product was successfully updated!"

    def test_func(self):
        """ Test user is superuser """
        return self.request.user.is_superuser


class DeleteProduct(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    """ View to delete an existing product """
    model = Product
    template_name = 'products/delete_product_confirm.html'
    success_url = reverse_lazy('manage_products')
    success_message = "Product Deleted!"

    def test_func(self):
        """ Test user is superuser """
        return self.request.user.is_superuser
