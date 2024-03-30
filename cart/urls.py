from django.urls import path
from .views import ViewShoppingCart
from . import views

urlpatterns = [
    path('', ViewShoppingCart.as_view(), name='cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('adjust/<item_id>/', views.adjust_cart, name='adjust_cart'),
    
]