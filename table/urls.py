from django.urls import path

from table.views import DataListView, DataCreateView, DataUpdateView, DataDeleteView, export_xls, export_csv

urlpatterns = [
    path('', DataListView.as_view(), name='index'),
    path('create/', DataCreateView.as_view(), name='create'),
    path('<int:pk>/edit/',
         DataUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/',
         DataDeleteView.as_view(), name='delete'),
    path('export-xls/', export_xls, name='export_xls'),
    path('export-csv', export_csv, name='export_csv'),
]
