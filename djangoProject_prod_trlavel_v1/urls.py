from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('firstapp.urls', 'firstapp'), namespace='firstapp')),
    path('', include(('mainapp.urls', 'mainapp'), namespace='mainapp')),
    path('', include(('travelblog.urls', 'travelblog'), namespace='travelblog')),
]
