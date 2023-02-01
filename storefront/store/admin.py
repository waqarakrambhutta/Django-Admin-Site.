from django.contrib import admin
from django.db.models import Count
from . import models
from django.urls import reverse
from django.utils.html import format_html


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display =  ['email','phone','order_count']
    list_per_page = 10

	
    @admin.display(ordering='order_count')
    def order_count(self,cart):
        url = reverse('admin:store_customer_changelist')
        return format_html('<a href="http://www.google.com">{}</a>',cart.order_count)
    

    def get_queryset(self,request):
        return super().get_queryset(request).annotate(
            order_count = Count('phone')
                                  
        )
