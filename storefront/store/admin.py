from django.contrib import admin
from . import models

# @admin.register(models.Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['title','unit_price','inventory_status']
#     list_editable=['unit_price']
#     list_per_page=10
    
#     @admin.display(ordering='inventory')
#     def inventory_status(self, product):
#         if product.inventory < 10:
#             return 'low'
#         return 'OK'

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['placed_at','payment_status','id_inc']
    list_per_page = 15
    
    def id_inc(self,order):
        new_id = order.customer_id
        return new_id + 1

admin.site.register(models.Collection)
# admin.site.register(models.Order,OrderAdmin)
# admin.site.register(models.Product,ProductAdmin)


