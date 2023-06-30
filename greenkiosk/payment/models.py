from django.db import models
from datetime import datetime

# Create your models here.
class Payment(models.Model):
    name = models.CharField(max_length = 32)
    payment_method = models.CharField(max_length = 32)
    transaction_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    created_at = models.DateTimeField(default=datetime(2023, 6, 18, 16, 35))
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    class Meta:
      verbose_name_plural = "Payment"