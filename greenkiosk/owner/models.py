from typing import Any
from django.db import models
from datetime import datetime

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    email = models.EmailField(verbose_name='Email Address')
    password = models.CharField('Password',max_length=6)
    storename = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    
    created_at = models.DateTimeField(default=datetime(2023, 6, 18, 16, 35))
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
      return self.name
