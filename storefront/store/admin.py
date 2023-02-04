from django.contrib import admin,messages
from tags.models import TaggedItem
from . import models
from django.contrib.contenttypes.admin import GenericTabularInline

class InventoryFilter(admin.SimpleListFilter):
    title = 'Inventory'
    parameter_name = 'Inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10','Low'),('>10 and <50', 'Ok'),('>50','High')
        ]
    
    def queryset(self, request, queryset):
        if self.value() == '<10':
            return queryset.filter(inventory__lte=10)
        elif self.value() == '>50':
            return queryset.filter(inventory__gt=10)
        elif self.value() == '>10 and <50':
            return queryset.filter(inventory__range=(11,49))  


class TagInline(GenericTabularInline):
    model = TaggedItem
    autocomplete_fields = ['tag']

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    actions = ['inventory_action']
    list_display = ['title','inventory','Inventory_status']
    list_filter= [InventoryFilter]
    list_per_page = 10
    inlines = [TagInline]
    search_fields = ['inventory__contains']

    def Inventory_status(self,separate):
        if separate.inventory <= 10:
            return 'Low'
        elif separate.inventory >=50:
            return 'High'
        else:
            return 'Ok'
        
    
    
    @admin.action(description='Clear Inventory')    
    def inventory_action(self, request, queryset):
        update_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{update_count} products were sucessfully updated.',
            messages.ERROR
        )


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['customer']
    list_display =['first_name','last_name','phone','membership']
    list_per_page = 10
    actions = ['membership_action']

    @admin.action(description='Finish the membership')    
    def membership_action(self, request, queryset):
        items = queryset.update(membership='_')
        self.message_user(
            request,
            f'{items} fields formated successfully.'
        )
        

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title','featured_product']
    search_fields = ['title']

# class OrderItemInline(admin.StackedInline):
class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    extra = 0
    min_num =1
    max_num = 10
    autocomplete_fields = ['product']


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    list_display = ['placed_at','payment_status','customer']
    list_per_page= 15
    inlines =[OrderItemInline]
