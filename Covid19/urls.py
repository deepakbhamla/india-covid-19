from django.conf.urls import url

from django.contrib import admin
from django.urls import path
from Crona import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name="home"),
    url('mapview/', views.MapView, name="symptoms"),
    url('news/', views.News, name="news"),
    

]
