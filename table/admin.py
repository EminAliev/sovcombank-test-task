from django.contrib import admin
from django.contrib.admin import ModelAdmin

from table.models import Data, ChangeLog


@admin.register(Data)
class DataAdminModel(ModelAdmin):
    list_display = ['product', 'phone_number', 'date', 'solution', 'comment']
    list_filter = ['phone_number', 'date']
    search_fields = ['product', 'phone_number']


@admin.register(ChangeLog)
class ChangeLogAdminModel(ModelAdmin):
    list_display = ['data_id', 'product', 'phone_number', 'date', 'solution', 'comment']
    list_filter = ['phone_number', 'date']
    search_fields = ['data_id', 'product', 'phone_number']
