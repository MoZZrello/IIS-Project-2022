from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #mozno potom zmazat
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.login_page, name="login"),
    path('register/', views.register_page, name="register"),
] 
