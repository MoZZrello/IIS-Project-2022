from django.forms import ModelForm, Field, ClearableFileInput
from django.utils.translation import gettext_lazy
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

Field.default_error_messages = {
    'required': gettext_lazy('Tohle pole je povinné'),
    'invalid': gettext_lazy('Hodnota není validní'),
}


class MyClearableFileInput(ClearableFileInput):
    template_name = 'widgets/customclearablefileinput.html'
    clear_checkbox_label = 'Smazat'
    initial_text = 'Aktuálně'
    input_text = 'Změnit'


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


class AllUsersForm(ModelForm):
    model = User
    fields = ['full_name', 'birthdate', 'phone_number', 'mail', 'user_verification', 'user_name', 'password', 'role_id', 'last login', 'date_joined', 'is_active', 'is_staff', 'is_superuser']
    full_name = forms.CharField(label="Celé jméno")
    phone_number = forms.CharField(label="Telefon")
    mail = forms.CharField(required=False, label="Email")
    profile_picture = forms.ImageField(required=False, label="Profilová fotografie", widget=MyClearableFileInput(attrs={'name': 'btn'}))

    class Meta:
        model = User
        fields = ['full_name', 'phone_number', 'mail', 'profile_picture']