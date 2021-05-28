from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterMixin

from table.filters import DataFilter
from table.models import Data


class DataListView(ListView, FilterMixin):
    model = Data
    template_name = 'table.html'
    filterset_class = DataFilter
    context_object_name = 'dates'


class DataCreateView(CreateView):
    model = Data
    template_name = 'create.html'
    success_url = '/'
    fields = ['product', 'phone_number', 'solution', 'comment']


class DataUpdateView(UpdateView):
    model = Data
    template_name = 'update.html'
    fields = ['product', 'phone_number', 'solution', 'comment']
    success_url = '/'


class DataDeleteView(DeleteView):
    model = Data
    template_name = 'delete.html'
    success_url = '/'
