from django.urls import path
from . import views
from .views import ViewWishList

urlpatterns = [
    path('', ViewWishList.as_view(), name='wishlist'),
    path('add-to-wishlist/<int:product_id>',
         views.add_to_wishlist, name='add_to_wishlist'),
    path('delete-from-wishlist/<int:product_id>', views.delete_from_wishlist, name='delete_from_wishlist'),

]