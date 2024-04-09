from django.views.generic import CreateView, TemplateView, ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import ContactMessage, Subscriber
from .forms import ContactForm, SubscribeForm

class ContactUsView(CreateView):
    model = ContactMessage
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('thank_you')


class ThankYouView(TemplateView):
    template_name = 'contact/thank_you.html'

class SubscribeFormView(SuccessMessageMixin, CreateView):
    model = Subscriber
    form_class = SubscribeForm
    template_name = 'footer.html'
    success_url = '/'
    success_message = "Thank you for subscribing!"

class InboxView(UserPassesTestMixin, ListView):
  
    model = ContactMessage
    template_name = 'contact/inbox.html'
    get_success_url = reverse_lazy('inbox')

    def get_queryset(self):

        if self.request.user.is_superuser:
            return ContactMessage.objects.all()

    def test_func(self):
        """ Test user is staff """
        if self.request.user.is_superuser:
            return True