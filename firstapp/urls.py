from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='firstpage'),
    path('authenticate/', views.authentication, name='authenticate'),
    path('authenticate-process/', views.authentication_process, name='authentication_process'),
    path('register/', views.register, name='register'),
    path('register-process', views.register_process, name='register_process'),
    path('logout/', views.user_logout, name='logout'),
]