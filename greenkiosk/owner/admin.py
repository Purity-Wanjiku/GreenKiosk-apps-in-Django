from django.contrib import admin
from .models import Vendor
# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name','username','email','password','storename','contact','created_at','updated_at')
admin.site.register(Vendor,VendorAdmin)
