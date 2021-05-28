import django_filters

from table.models import Data


class DataFilter(django_filters.FilterSet):
    comment = django_filters.CharFilter(lookup_expr='iexact', label='Комментарий')

    class Meta:
        model = Data
        fields = ['date', 'product', 'phone_number', 'solution', 'comment']
