from django.urls import path
from .views import UserProfileView, AdminOrdersView, AdminOrderDetailView

urlpatterns = [
    path('', UserProfileView.as_view(), name='profile'),
    path('orders/', AdminOrdersView.as_view(), name='orders'),
    path('order/<int:pk>/', AdminOrderDetailView.as_view(), name='order_detail'),
    
]