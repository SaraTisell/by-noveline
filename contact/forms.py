from django import forms
from .models import ContactMessage, Subscriber


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = [
            'name',
            'email',
            'regarding_an_order',
            'order_number',
            'title',
            'message',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'email': 'Email',
            'order_number': 'Order Number',
            'title': 'Subject',
            'message': 'Wrtie your message here',
        }

        labels = {
         'regarding_an_order': 'Does your question apply to an order?'
        }

        for field, placeholder in placeholders.items():
            self.fields[field].widget.attrs['placeholder'] = placeholder

        for field in self.fields:
            if field != 'regarding_an_order':
                self.fields[field].label = False
                self.fields[field].widget.attrs['class'] = 'contact-form-input'

        for field, label in labels.items():
            self.fields[field].label = label


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Your Email'
        self.fields['email'].label = False
