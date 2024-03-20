from django.urls import path
from .views import AllProducts, ProductDetail, SearchResultsView

urlpatterns = [
    path('', AllProducts.as_view(), name='products'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('<slug:slug>/', ProductDetail.as_view(), name='product_detail'),

]