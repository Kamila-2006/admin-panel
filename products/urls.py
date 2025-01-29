from django.urls import path
from . import views


app_name = 'products'

urlpatterns = [
    path('products-list/', views.products_list, name='list'),
    path('add-product/', views.create_product, name='create'),
    path('product-update/<int:pk>/', views.product_update, name='update'),
    path('product-detail/<int:pk>/', views.product_detail, name='detail'),
    path('product-delete/<int:pk>/', views.delete_product, name='delete'),
]