from django.contrib import admin
from .models import AddToCart
# Register your models here.
class AddToCartAdmin(admin.ModelAdmin):
    list_display = ('name','quantity','product_price','payment_method','delivery_cost','created_at','updated_at')
admin.site.register(AddToCart,AddToCartAdmin)