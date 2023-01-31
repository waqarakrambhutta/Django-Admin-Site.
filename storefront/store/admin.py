from django.contrib import admin
from . import models

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','unit_price','last_update','collection_title']
    list_select_related = ['collection']
    def collection_title(self,link):
        return link.collection.title

admin.site.register(models.Product,ProductAdmin)