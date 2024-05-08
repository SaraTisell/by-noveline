from django.urls import path
from .views import (
    AllProducts, ProductDetail,
    SearchResultsView, AddNewProduct,
    UpdateProduct, DeleteProduct
)

urlpatterns = [
    path('', AllProducts.as_view(), name='products'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('management/', AddNewProduct.as_view(), name='manage_products'),
    path('<int:pk>/update/', UpdateProduct.as_view(), name='update_product'),
    path('<int:pk>/delete/', DeleteProduct.as_view(), name='delete_product'),
    path('<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
]
