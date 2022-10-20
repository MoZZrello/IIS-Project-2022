import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter

from .models import *


class AnimalFilter(django_filters.FilterSet):
    animal_name = CharFilter(field_name="animal_name", lookup_expr="icontains", label="Jméno mazlíčka")
    species = CharFilter(field_name="species", lookup_expr="icontains", label="Druh")
    breed = CharFilter(field_name="breed", lookup_expr="icontains", label="Plemeno")
    age = NumberFilter(field_name="age", lookup_expr="exact", label="Věk")

    class Meta:
        model = Animal
        fields = ['animal_name', 'species', 'breed', 'age']

