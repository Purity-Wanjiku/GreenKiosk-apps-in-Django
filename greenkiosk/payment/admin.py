from django.contrib import admin
from .models import Payment
# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name','payment_method','amount','created_at','updated_at')
admin.site.register(Payment,PaymentAdmin)
