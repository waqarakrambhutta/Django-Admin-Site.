from django.contrib import admin
from django.http import HttpRequest
from django.db.models import Count
from django.utils.html import format_html
from . import models

class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10','Low')
        # we can also write more tuples here
        ]

    def queryset(self, request, queryset):
        if self.value()=='<10':
            return queryset.filter(inventory__lt= 10)

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'unit_price',
                    'inventory',
                    'inventory_status',
                    'collection_title'
                    ]
    
    list_editable = ['unit_price']
    list_filter = ['collection','last_update',InventoryFilter]
    list_per_page = 10
    ordering = ['title']
    search_fields = ['inventory__lte']
    list_select_related = ['collection']

    def collection_title(self,product):
        return product.collection.title
    
    def inventory_status(self,product):
        if product.inventory >= 10:
            return 'OK'
        return 'Low'



@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','membership']
    ordering = ['first_name','last_name']
    search_fields = ['first_name__istartswith','last_name__istartswith']

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
        


