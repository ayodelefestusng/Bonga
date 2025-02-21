from django.contrib import admin
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import *



# admin.site.register(User,UserAdmin)
# admin.site.register(CustomGroup)


class ModelInline(admin.TabularInline):
    model = Model
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ModelInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Customer)




admin.site.register(Invoice)

class InventoryAdmin(admin.ModelAdmin):
    # pass
    list_display = ('model', 'vin', 'balance')
    # fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
admin.site.register(Inventory,InventoryAdmin )

class transactionAdmin(admin.ModelAdmin):
    # pass
    list_display = ( 'vin', 'transaction_type')
    # fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
admin.site.register(Transaction,transactionAdmin )

