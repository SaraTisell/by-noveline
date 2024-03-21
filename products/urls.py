from django.urls import path
from .views import AllProducts, ProductDetail, SearchResultsView, AddNewProduct

urlpatterns = [
    path('', AllProducts.as_view(), name='products'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('management/', AddNewProduct.as_view(), name='manage_products'),
    path('<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
]