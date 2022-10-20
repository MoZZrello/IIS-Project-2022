from django.forms import ModelForm, Field
from django.utils.translation import gettext_lazy
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

Field.default_error_messages = {
    'required': gettext_lazy('Tohle pole je povinné'),
    'invalid': gettext_lazy('Hodnota není validní'),
}


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


class ProfileForm(ModelForm):

    class Meta:
        model = User
        fields = ['full_name', 'phone_number', 'email']
