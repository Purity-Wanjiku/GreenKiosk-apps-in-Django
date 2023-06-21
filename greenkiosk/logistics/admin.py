from django.contrib import admin
from .models import Delivery
# Register your models here.
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('name','price','status','delivery_method','duration','delivery_address','created_at','updated_at')
admin.site.register(Delivery,DeliveryAdmin)
