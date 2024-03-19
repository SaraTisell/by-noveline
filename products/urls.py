from django.urls import path
from .views import AllProducts, ProductDetail

urlpatterns = [
    path('', AllProducts.as_view(), name='products'),
    path('<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
    
]