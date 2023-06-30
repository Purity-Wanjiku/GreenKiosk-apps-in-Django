from django.db import models

# Create your models here.
class Order(models.Model):
    order_number = models.IntegerField()
    order_total = models.IntegerField()
    customer = models.CharField(max_length=32)
    delivery_location = models.CharField(max_length=100)
    product_id = models.IntegerField()
    payment_options = models.CharField(max_length=100)
    order_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"Order {self.order_number}"