import csv
from datetime import datetime

import xlwt
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterMixin

from table.filters import DataFilter
from table.models import Data
from table.queries import count_data, last_data, client_approved


class DataListView(ListView, FilterMixin):
    model = Data
    template_name = 'table.html'
    filterset_class = DataFilter
    context_object_name = 'dates'

    def get_queryset(self):
        search_query = self.request.GET.get('search', '')
        if search_query:
            qs = Data.objects.filter(Q(product__icontains=search_query) | Q(phone_number__icontains=search_query) | Q(
                solution__icontains=search_query) | Q(comment__icontains=search_query))
        else:
            qs = Data.objects.all()
        return qs


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


def export_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="data.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Заявки')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Дата', 'Продукт', 'Номер телефона', 'Решение', 'Комментарий']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = Data.objects.all().values_list('date', 'product', 'phone_number', 'solution', 'comment')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if isinstance(row[col_num], datetime):
                ws.write(row_num, col_num, row[col_num].strftime("%Y-%m-%d %H:%M"), font_style)
            else:
                ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response


def export_csv(request):
    model_class = Data
    fields = [f.name for f in model_class._meta.fields]

    timestamp = datetime.now().isoformat()

    response = HttpResponse(content_type="text/csv")
    response[
        "Content-Disposition"
    ] = f"attachment; filename={timestamp}.csv"
    writer = csv.writer(response)

    writer.writerow(fields)

    for row in model_class.objects.values(*fields):
        writer.writerow([row[field] for field in fields])

    return response


def count_month_view(request):
    return render(request, 'count_month.html', {'data': count_data()})


def last_data_view(request):
    return render(request, 'last_data.html', {'data': last_data()})


def client_approved_view(request):
    return render(request, 'client_approved.html', {'data': client_approved()})
