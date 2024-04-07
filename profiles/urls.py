from django.urls import path
from .views import UserProfileView, AdminOrdersView, AdminOrderDetailView, AdminDeleteOrder

urlpatterns = [
    path('', UserProfileView.as_view(), name='profile'),
    path('orders/', AdminOrdersView.as_view(), name='orders'),
    path('order/<int:pk>/', AdminOrderDetailView.as_view(), name='order_detail'),
    path('order/<int:pk>/delete/', AdminDeleteOrder.as_view(), name='delete_order'),
]