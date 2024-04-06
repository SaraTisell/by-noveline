from django.views.generic import UpdateView
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import UserProfile
from .forms import UserDeliveryInfo

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
        print(orders)
        return context
