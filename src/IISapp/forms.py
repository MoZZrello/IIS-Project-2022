from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from models import User, User_roles


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['user_name', 'birthdate', 'phone_numb', 'mail', 'password1', 'password2']
