
from django.urls import path, include
from . import views

urlpatterns = [
    path('products/', views.products),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    path ('cart/', views.cart),
    path('cart/<int:pk>/', views.CartDetail.as_view()),
   
]
