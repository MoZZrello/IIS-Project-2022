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


class MyDateInput(forms.DateInput):
    input_type = 'date'
    format = ["%d.%m.%Y"]


class MyAnimalChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.animal_name


class MyUserChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.full_name


class CreateUserForm(UserCreationForm):
    birthdate = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y'),
        input_formats=['%d.%m.%Y']
    )
    phone_number = forms.CharField(label="Telefon", required=False)
    mail = forms.CharField(label="Email", required=False)

    class Meta:
        model = User
        fields = ['full_name', 'user_name', 'mail', 'phone_number', 'birthdate', 'password1', 'password2']


class CreateWalkForm(ModelForm):
    user_name = MyUserChoiceField(queryset=User.objects.all())
    animal = MyAnimalChoiceField(queryset=Animal.objects.all())

    class Meta:
        model = outing_reservation
        widgets = {'outing_start': forms.DateTimeInput(), 'outing_end': forms.DateTimeInput()}
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CreateWalkForm, self).__init__(*args, **kwargs)
        self.fields['user_name'].label = "Dobrovolník"
        self.fields['animal'].label = "Zvířátko"
        self.fields['outing_start'].label = "Začátek"
        self.fields['outing_end'].label = "Konec"
        self.fields['outing_verification'].label = "Ověření"
        self.fields['outing_assigned'].label = "Je přidělené"


class CreateAnimalForm(ModelForm):
    capture_date = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y'),
        input_formats=['%d.%m.%Y']
    )
    image = forms.ImageField(
        required=False,
        label="Fotografie",
        widget=MyClearableFileInput(attrs={'name': 'btn'})
    )

    class Meta:
        model = Animal
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CreateAnimalForm, self).__init__(*args, **kwargs)
        self.fields['animal_name'].label = "Jméno zvířátka"
        self.fields['species'].label = "Druh"
        self.fields['breed'].label = "Rasa"
        self.fields['age'].label = "Věk"
        self.fields['animal_description'].label = "Popis"
        self.fields['capture_date'].label = "Datum odchycení"
        self.fields['outing_suitable'].label = "Vhodný pro procházky"
        self.fields['animal_verification'].label = "Přítomen v útulku"


class CreateVetRequestForm(ModelForm):
    contractor = MyUserChoiceField(queryset=User.objects.all())
    solver = MyUserChoiceField(queryset=User.objects.all())
    animal = MyAnimalChoiceField(queryset=Animal.objects.all())
    datetime_start = forms.DateTimeField(
        widget=forms.DateTimeInput(format='%d.%m.%Y %H:%M'),
        input_formats=['%d.%m.%Y %H:%M']
    )
    datetime_end = forms.DateTimeField(
        widget=forms.DateTimeInput(format='%d.%m.%Y %H:%M'),
        input_formats=['%d.%m.%Y %H:%M']
    )

    class Meta:
        model = Requests
        fields = '__all__'
        exclude = ('outing_assigned', 'request_verification',)

    def __init__(self, *args, **kwargs):
        super(CreateVetRequestForm, self).__init__(*args, **kwargs)
        self.fields['contractor'].label = "Zadavatel"
        self.fields['solver'].label = "Řešitel"
        self.fields['animal'].label = "Zvířátko"
        self.fields['datetime_start'].label = "Začátek"
        self.fields['datetime_end'].label = "Konec"
        self.fields['veterinary_req'].label = "Požadavek na veterináře"
        self.fields['request_name'].label = "Název požadavku"
        self.fields['request_description'].label = "Popis požadavku"


class ProfileForm(ModelForm):
    full_name = forms.CharField(label="Celé jméno")
    phone_number = forms.CharField(label="Telefon", required=False)
    mail = forms.CharField(required=False, label="Email")
    profile_picture = forms.ImageField(required=False, label="Profilová fotografie",
                                       widget=MyClearableFileInput(attrs={'name': 'btn'}))

    class Meta:
        model = User
        fields = ['full_name', 'phone_number', 'mail', 'profile_picture']


class AllUsersForm(ModelForm):
    model = User
    fields = ['full_name', 'birthdate', 'phone_number', 'mail', 'user_verification', 'user_name', 'password', 'role_id',
              'last login', 'date_joined', 'is_active', 'is_staff', 'is_superuser']
    full_name = forms.CharField(label="Celé jméno")
    phone_number = forms.CharField(label="Telefon")
    mail = forms.CharField(required=False, label="Email")
    profile_picture = forms.ImageField(required=False, label="Profilová fotografie",
                                       widget=MyClearableFileInput(attrs={'name': 'btn'}))

    class Meta:
        model = User
        fields = ['full_name', 'phone_number', 'mail', 'profile_picture']


class EditVetRequest(ModelForm):
    model = Requests
    fields = ('contractor', 'solver', 'animal', 'datetime_start', 'datetime_end', 'veterinary_req', 'request_name',
              'request_description', 'request_verification', 'outing_assigned')
    datetime_end = forms.DateField(label="Konec")
    request_name = forms.CharField(label="Název")
    request_description = forms.CharField(required=False, label="Popis")

    class Meta:
        model = Requests
        fields = ['datetime_end', 'request_name', 'request_description']
