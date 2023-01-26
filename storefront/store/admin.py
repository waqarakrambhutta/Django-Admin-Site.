from django.contrib import admin
from . import models

# @admin.register(models.Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['title','unit_price','inventory_status','collection_title']
#     list_editable=['unit_price']
#     list_per_page=10
#     list_select_related = ['collection']
    
#     def collection_title(self,product):
#         return product.collection.title

#     @admin.display(ordering='inventory')
#     def inventory_status(self, product):
#         if product.inventory < 10:
#             return 'low'
#         return 'OK'


# admin.site.register(models.Order,OrderAdmin)
# admin.site.register(models.Product,ProductAdmin)

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display =['id','placed_at','customer']
    list_per_page = 15
    list_select_related = ['customer']


