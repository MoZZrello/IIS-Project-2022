from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class CreateUserForm(UserCreationForm):
    birthdate = forms.DateField(widget=DateInput)

    class Meta:
        model = User
        widgets = {'birthdate': DateInput()}
        fields = ['full_name', 'user_name', 'mail', 'phone_number', 'birthdate', 'password1', 'password2']


class CreateWalkForm(ModelForm):

    class Meta:
        model = outing_reservation
        widgets = {'outing_start': forms.DateTimeInput(), 'outing_end': forms.DateTimeInput()}
        fields = '__all__'
