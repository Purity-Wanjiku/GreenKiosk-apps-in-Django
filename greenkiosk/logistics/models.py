from django.db import models
from datetime import datetime

# Create your models here.
class Delivery(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    status = models.CharField(max_length = 32)
    delivery_method = models.TextField()
    duration = models.DurationField()
    delivery_address = models.CharField(max_length=200)
    
    created_at = models.DateTimeField(default=datetime(2023, 6, 18, 16, 35))
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
        
    class Meta:
      verbose_name_plural = "Delivery"
    
    
