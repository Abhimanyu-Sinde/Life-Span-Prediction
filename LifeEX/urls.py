from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result/', views.result, name='result'),
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
]