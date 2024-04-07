from django.urls import path
from .views import ContactUsView, ThankYouView

urlpatterns = [
    path('', ContactUsView.as_view(), name='contact'),
    path('thank_you/', ThankYouView.as_view(), name='thank_you'),
]