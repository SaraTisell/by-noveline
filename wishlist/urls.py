from django.urls import path
from . import views
from .views import ViewWishList, RemoveItemFromWishList

urlpatterns = [
    path('', ViewWishList.as_view(), name='wishlist'),
    path('add-to-wishlist/<int:product_id>',
         views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlistitem/<int:pk>/delete', RemoveItemFromWishList.as_view(), name='wishlist_item_delete'),

]