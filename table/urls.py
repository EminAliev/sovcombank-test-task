from django.urls import path

from table.views import DataListView, DataCreateView, DataUpdateView, DataDeleteView

urlpatterns = [
    path('', DataListView.as_view(), name='index'),
    path('create/', DataCreateView.as_view(), name='create'),
    path('<int:pk>/edit/',
         DataUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/',
         DataDeleteView.as_view(), name='delete'),
]
