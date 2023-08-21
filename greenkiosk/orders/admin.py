from django.contrib import admin
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number','order_total','customer','delivery_location','payment_options','order_date')
admin.site.register(Order,OrderAdmin)
    