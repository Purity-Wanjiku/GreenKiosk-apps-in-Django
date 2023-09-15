from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# from inventory.models import Product


# Create your models here.
class Cart(models.Model ):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    # product = models.ManyToManyField(Product)
    # name = models.CharField(max_length = 32)
    quantity = models.PositiveIntegerField()
    product_price = models.DecimalField(max_digits = 6, decimal_places = 2)
    payment_method = models.CharField(max_length=50)
    delivery_cost = models.DecimalField(max_digits = 6, decimal_places = 2)
    
    created_at = models.DateTimeField(default=datetime(2023, 6, 18, 16, 35))
    updated_at = models.DateTimeField(auto_now=True)
    

    def add_product(self, Product):
        self.products.add(Product)
        self.save()
        return self
    
    def product_total(self):
        products = self.products
        total = 0
        # for product in products:
        #     total += product.price
        # return total
    
    # or 

        total = sum([product.price for product in self.products])


