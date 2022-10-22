import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter

from .models import *
from django.conf import settings


class AnimalFilter(django_filters.FilterSet):
    animal_name = CharFilter(field_name="animal_name", lookup_expr="icontains", label="Jméno mazlíčka")
    species = CharFilter(field_name="species", lookup_expr="icontains", label="Druh")
    breed = CharFilter(field_name="breed", lookup_expr="icontains", label="Plemeno")
    age = NumberFilter(field_name="age", lookup_expr="exact", label="Věk")

    class Meta:
        model = Animal
        fields = ['animal_name', 'species', 'breed', 'age']


class UserFilter(django_filters.FilterSet):
    full_name = CharFilter(field_name="full_name", lookup_expr="icontains", label="Jméno")
    phone_number = CharFilter(field_name="phone_number", lookup_expr="icontains", label="Telefoní č.")
    mail = CharFilter(field_name="mail", lookup_expr="icontains", label="E-mail")
    user_name = CharFilter(field_name="user_name", lookup_expr="icontains", label="Login")

    class Meta:
        model = User
        fields = ['full_name', 'phone_number', 'mail', 'user_name']


class OutingsFilter(django_filters.FilterSet):
    user_name = CharFilter(field_name="user_name__user_name", lookup_expr="icontains", label="Dobrovolník")
    animal = CharFilter(field_name="animal__animal_name", lookup_expr="icontains", label="Zvířátko")
    outing_start = django_filters.DateFilter(field_name='outing_start',
                                             lookup_expr='contains',
                                             label='Dátum začátku',
                                             input_formats=['%d.%m.%Y'])
    outing_end = django_filters.DateFilter(field_name='outing_end',
                                           lookup_expr='contains',
                                           label='Dátum konce',
                                           input_formats=['%d.%m.%Y'])

    class Meta:
        model = outing_reservation
        fields = ['user_name', 'animal', 'outing_start', 'outing_end']
