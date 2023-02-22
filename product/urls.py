
from django.urls import path, include
from . import views

urlpatterns = [
    path('products/', views.products),
    path('product/<int:pk>/', views.product_detail),
    path ('cart/', views.cart),
    path('cart/<int:pk>/', views.cart_detail),
   
]
