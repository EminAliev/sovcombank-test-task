from django.views.generic import ListView
from django_filters.views import FilterMixin

from table.filters import DataFilter
from table.models import Data


class DataListView(ListView, FilterMixin):
    model = Data
    template_name = 'table.html'
    filterset_class = DataFilter
    context_object_name = 'dates'

