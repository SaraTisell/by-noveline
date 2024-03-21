from django.urls import path
from .views import AllProducts, ProductDetail, SearchResultsView, AddNewProduct, UpdateProduct

urlpatterns = [
    path('', AllProducts.as_view(), name='products'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('management/', AddNewProduct.as_view(), name='manage_products'),
    path('<int:pk>/update/', UpdateProduct.as_view(), name='update_product'),
    path('<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
]