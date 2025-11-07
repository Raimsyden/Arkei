
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.main, name='main'),
    path('cuenta/', views.cuenta, name='cuenta'),
    path('producto/', views.producto, name='productos'),
    path('register/', views.registro, name='register'),
    path('about/', views.about, name='about'),
    path('', views.login, name='login'),
    
]
