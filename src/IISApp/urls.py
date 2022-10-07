from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #mozno potom zmazat
    path('about', views.about, name="about"),
    path('contact', views.concact, name="contact"),
] 
