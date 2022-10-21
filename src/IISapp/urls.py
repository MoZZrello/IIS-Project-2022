from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name="about"),
    path('animal/all/<int:animalid>/', views.animal_profile, name="animal_profile"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_page, name="register"),
    path('profil/', views.user_profile, name="profil"),
    path('walk/create/', views.create_walk, name="create_walk"),
    path('walk/dashboard/', views.walks_dashboard, name="walks_dashboard"),
    path('walk/update/<str:pk>/', views.update_walk, name="update_walk"),
    path('walk/delete/<str:pk>/', views.delete_walk, name="delete_walk"),
    path('walk/reservation/assign/<int:resid>/<int:name>/', views.assign_walk, name="assign_walk"),
    path('walk/reservation/unassign/<int:resid>/', views.unassign_walk, name="unassign_walk"),
    path('walk/reservation/', views.reservation, name="reservation"),
    path('animal/all/', views.all_animals, name="all_animals"),
    path('animal/add/', views.add_animals, name="add_animals"),
    path('animal/update/<str:pk>/', views.update_animals, name="update_animals"),
    path('animal/delete/<str:pk>/', views.delete_animals, name="delete_animals"),
    path('volunteer/verification/', views.volunteer_verification, name="volunteer_verification"),
    path('volunteer/verification/verify/<int:userid>/', views.verify_volunteer, name="verify_volunteer"),
    path('volunteer/verification/unverify/<int:userid>/', views.unverify_volunteer, name="unverify_volunteer"),
    path('admin_site/', views.admin_site, name="admin_site"),
] 
