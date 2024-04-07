from django.views.generic import CreateView, TemplateView
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