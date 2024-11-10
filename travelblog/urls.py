from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('blog/add-post/', views.add_post, name='add_post'),

    path('blog/process-add-post/', views.process_add_post, name='process_add_post'),
]