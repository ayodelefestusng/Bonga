
# Register your models here.
from django.contrib import admin

from .models import PromoCode,Product,CreateGift,Winning_Code

admin.site.register(PromoCode)
# admin.site.register(Product)
admin.site.register(CreateGift)
admin.site.register(Winning_Code)




class PromoCode(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["code"]}),]
   

    list_display = ["code", "gift", "status"]
    # list_filter = ["pub_date"]
    # search_fields = ["question_text"]
    
    
    
