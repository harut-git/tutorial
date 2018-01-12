import django_filters
from models import Fruit


class FruitFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(name="fruit_name")
    promoted = django_filters.BooleanFilter(name="promoted_type")

    class Meta:
        model = Fruit
        fields = ['name', 'promoted', 'language_code']