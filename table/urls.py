from django.urls import path

from table.views import DataListView

urlpatterns = [
    path('', DataListView.as_view(), name='index')
]
