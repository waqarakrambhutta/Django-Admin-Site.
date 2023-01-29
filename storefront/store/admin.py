from django.contrib import admin
from . import models

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','order']
    list_select_related = ['order']

    