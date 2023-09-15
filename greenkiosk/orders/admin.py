from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('ordered','order_number','order_total','customer','delivery_location','payment_options','start_date','ordered_date')
admin.site.register(Order,OrderAdmin)



class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('ordered','quantity')
admin.site.register(OrderItem,OrderItemAdmin)
   