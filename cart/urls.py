from django.urls import path
from .views import ViewShoppingCart
from . import views

urlpatterns = [
    path('', ViewShoppingCart.as_view(), name='cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('adjust/<cart_key>/', views.adjust_cart, name='adjust_cart'),
    path('remove/<cart_key>/', views.remove_from_cart, name='remove_from_cart'),
    
]