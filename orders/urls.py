from django.urls import path
from . import views


app_name = 'orders'

urlpatterns = [
    path('orders-list/', views.order_list, name='list'),
    path('order-detail/<int:pk>/', views.order_detail, name='detail'),
]