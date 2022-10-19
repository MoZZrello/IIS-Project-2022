import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


class AnimalFilter(django_filters.FilterSet):
    capture_date_after = DateFilter(field_name="capture_date", lookup_expr="gte")
    capture_date_before = DateFilter(field_name="capture_date", lookup_expr="lt")
    animal_name = CharFilter(field_name="animal_name", lookup_expr="icontains")
    species = CharFilter(field_name="species", lookup_expr="icontains")
    breed = CharFilter(field_name="breed", lookup_expr="icontains")

    class Meta:
        model = Animal
        fields = ['animal_name', 'species', 'breed', 'age']
