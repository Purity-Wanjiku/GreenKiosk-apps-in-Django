from django.db import models

# Create your models here.
class Rating(models.Model):
    name = models.CharField(max_length=32)
    review_message = models.TextField()
    sender = models.CharField(max_length=32)
    star_rating = models.DecimalField(max_digits=10,decimal_places=2 )
    value = models.CharField(max_length=32)
    date = models.DateField(auto_now=True)
    
def __str__(self):
      return self.name