from django.contrib import admin
from django.http import HttpRequest
from django.db.models import Count
from . import models


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display =['title','product_count']

    @admin.display(ordering='product_count')
    def product_count(self,collection):
        return collection.product_count
    
    def get_queryset(self,request):
        return super().get_queryset(request).annotate(
            product_count = Count('product')
                                  
        )
        


# admin.site.register(models.Collection,CollectionAdmin)