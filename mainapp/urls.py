from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('main/add-trip', views.add_trip, name='add_trip'),
    path('proces-add-trip', views.process_add_trip, name='process_add_trip'),

    path('main/download/<int:id>/', views.download, name='download'),

    path('main/statistics/', views.statistics, name='statistics'),

]