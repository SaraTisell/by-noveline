from django.urls import path
from .views import AllProducts

urlpatterns = [
    path('', AllProducts.as_view(), name='products')
    
]