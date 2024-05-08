from django.views.generic import UpdateView, ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import UserProfile
from .forms import UserDeliveryInfo
from checkout.forms import OrderForm

from checkout.models import Order


class UserProfileView(UpdateView):
    template_name = 'profiles/profile.html'
    model = UserProfile
    form_class = UserDeliveryInfo
    success_url = reverse_lazy('profile')

    def get_object(self):
        return get_object_or_404(UserProfile, user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Your Delivery info has been updated!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        orders = profile.orders.all()
        context['orders'] = orders
        return context


class AdminOrdersView(UserPassesTestMixin, ListView):
    model = Order
    template_name = 'profiles/orders.html'
    get_success_url = reverse_lazy('orders')

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Order.objects.all()

    def test_func(self):
        if self.request.user.is_superuser:
            return True


class AdminOrderDetailView(UserPassesTestMixin, DetailView):
    model = Order
    template_name = 'profiles/order_detail.html'

    def test_func(self):
        if self.request.user.is_superuser:
            return True


class AdminDeleteOrder(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Order
    template_name = 'profiles/delete_order_confirm.html'
    success_url = reverse_lazy('orders')
    success_message = "The order was successfully deleted!"

    def test_func(self):
        if self.request.user.is_superuser:
            return True
