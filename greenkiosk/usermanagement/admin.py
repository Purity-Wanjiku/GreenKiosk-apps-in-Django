from django.contrib import admin
from .models import Customer
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','contact','email','password','username','created_at','updated_at')
admin.site.register(Customer,CustomerAdmin)