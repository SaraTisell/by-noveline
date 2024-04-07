from django.views.generic import CreateView, TemplateView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import ContactMessage
from .forms import ContactForm

class ContactUsView(CreateView):
    model = ContactMessage
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('thank_you')


class ThankYouView(TemplateView):
    template_name = 'contact/thank_you.html'
