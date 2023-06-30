from django.db import models

# Create your models here.
class Notification(models.Model):
    name = models.CharField(max_length=32)
    message = models.TextField()
    recipient = models.CharField(max_length=32)
    date = models.DateField(auto_now=True)
    
    
    def __str__(self):
      return self.name