from django.urls import path
from . import views


app_name = 'orders'

urlpatterns = [
    path('orders-list/', views.order_list, name='list'),
    path('order-update/<int:pk>/', views.edit_order, name='update'),
    path('order-detail/<int:pk>/', views.order_detail, name='detail'),
    path('delete_item/<int:pk>/', views.delete_order_item, name='delete_item'),
]