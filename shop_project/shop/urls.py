from django.urls import path
from . import views

urlpatterns = [
    #  старые маршруты
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('author/', views.author, name='author'),
    
    # Новые маршруты для магазина 
    path('catalog/', views.product_list, name='product_list'), 
    path('catalog/<int:pk>/', views.product_detail, name='product_detail'), 
]
