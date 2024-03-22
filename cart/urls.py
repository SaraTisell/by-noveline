from django.urls import path
from .views import ViewShoppingCart

urlpatterns = [
    path('', ViewShoppingCart.as_view(), name='cart'),
    
]