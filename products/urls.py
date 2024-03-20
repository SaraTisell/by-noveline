from django.urls import path
from .views import AllProducts, ProductDetail, SearchResultsView, AddNewProduct

urlpatterns = [
    path('', AllProducts.as_view(), name='products'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('add/', AddNewProduct.as_view(), name='add_product'),
    path('<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
]