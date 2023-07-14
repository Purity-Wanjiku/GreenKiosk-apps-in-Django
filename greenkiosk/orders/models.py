from django.db import models
from payment.models import Payment
from cartsystem.models import Cart
from usermanagement.models import Customer
from logistics.models import Delivery

# Create your models here.
class Order(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.PROTECT, null=True)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, null=True)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, null=True)
    logistics = models.ManyToManyField(Delivery)

    order_number = models.IntegerField()
    order_total = models.IntegerField()
    customer = models.CharField(max_length=32)
    delivery_location = models.CharField(max_length=100)
    product_id = models.IntegerField()
    payment_options = models.CharField(max_length=100)
    order_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"Order {self.order_number}" 