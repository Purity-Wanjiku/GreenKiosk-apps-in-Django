from django.contrib import admin
from .models import Cart
# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ('quantity','product_price','payment_method','delivery_cost','created_at','updated_at')
admin.site.register(Cart,CartAdmin)
