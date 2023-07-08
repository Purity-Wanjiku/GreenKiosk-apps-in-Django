from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null=True )

    name = models.CharField('Name', max_length=32)
    contact = models.CharField(max_length=15)
    email = models.EmailField(verbose_name='Email Address')
    password = models.CharField('Password',max_length=6)
    username = models.CharField('User name', max_length=32)
    
    created_at = models.DateTimeField(default=datetime(2023, 6, 18, 16, 35))
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
     return self.name
 