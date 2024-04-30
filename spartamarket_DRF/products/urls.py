from django.urls import path
from .views import ProductListView, ProductDetailView, CreateProductView, UpdateProductView, DeleteProductView
from rest_framework.response import Response


urlpatterns = [
    path('api/products/', ProductListView.as_view(), name='product_list'),
    path('api/products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('api/products/', CreateProductView.as_view(), name='create_product'),
    path('api/products/<int:pk>/', UpdateProductView.as_view(), name='update_product'),
    path('api/products/<int:pk>/', DeleteProductView.as_view(), name='delete_product'),

]
