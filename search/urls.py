from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='search-home'),
    path('about/', views.about, name='search-about'),
    path('classes/', views.classes, name='search-classes'),
    path('register/', views.register, name='register'),
]
