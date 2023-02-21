
from django.urls import path, include
from . import views

urlpatterns = [
    path('products/', views.products),
    path('products/<int:pk>/', views.ProductDetail.as_view()),
    path('cart/', views.cart),
]
