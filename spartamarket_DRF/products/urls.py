from django.urls import path
from .views import ProductListView, ProductDetailView, CreateProductView, UpdateProductView, DeleteProductView

urlpatterns = [
    path('api/products/', ProductListView.as_view(), name='product_list'),
    path('api/products/<int:pk>/',ProductDetailView.as_view(), name='product_detail'),
    path('api/products/create/', CreateProductView.as_view(), name='create_product'),
    path('api/products/<int:pk>/update/',UpdateProductView.as_view(), name='update_product'),
    path('api/products/<int:pk>/delete/',DeleteProductView.as_view(), name='delete_product'),
]
