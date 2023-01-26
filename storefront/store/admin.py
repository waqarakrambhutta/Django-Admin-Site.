from django.contrib import admin
from django.http import HttpRequest
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode
from . import models


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display =['title','product_count']

    @admin.display(ordering='product_count')
    def product_count(self,collection):

        url = (reverse('admin:store_product_changelist') 
               + '?'
               + urlencode({
                'collection__id': str(collection.id)
               }))
               
        return format_html('<a href="{}">{}</a>',url, collection.product_count)
    
    
    def get_queryset(self,request):
        return super().get_queryset(request).annotate(
            product_count = Count('product')
                                  
        )
        


# admin.site.register(models.Collection,CollectionAdmin)