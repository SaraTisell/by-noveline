from django.urls import path
from .views import ContactUsView, ThankYouView, SubscribeFormView, InboxView

urlpatterns = [
    path('', ContactUsView.as_view(), name='contact'),
    path('thank_you/', ThankYouView.as_view(), name='thank_you'),
    path('subscribe/', SubscribeFormView.as_view(), name='subscribe'),
    path('inbox/', InboxView.as_view(), name='inbox'),
]
