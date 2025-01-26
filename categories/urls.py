from django.urls import path
from . import views


app_name = 'categories'

urlpatterns = [
    path('category-list/', views.category_list, name='list'),
    path('create-category/', views.create_category, name='create'),
    path('category-update/<int:pk>/', views.category_update, name='update'),
    path('category-detail/<int:pk>/', views.category_detail, name='detail'),
    path('category-delete/<int:pk>/', views.delete_category, name='delete'),
]