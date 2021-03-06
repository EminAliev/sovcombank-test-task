from django.contrib import admin
from django.contrib.admin import ModelAdmin

from table.models import Data


@admin.register(Data)
class DataAdminModel(ModelAdmin):
    list_display = ['product', 'phone_number', 'date', 'solution', 'comment', 'author']
    list_filter = ['phone_number', 'date']
    search_fields = ['product', 'phone_number']
    ordering = ('date', 'phone_number')
    readonly_fields = ('date',)
