from django.db import models
from payment.models import Payment
from django.db import models
from django.conf import settings 
# from cartsystem.models import Cart
# from usermanagement.models import Customer
# from logistics.models import Delivery
from items.models import Product


class OrderItem(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        ordered = models.BooleanField(default=False)
        item = models.ForeignKey(Product, on_delete=models.CASCADE)
        quantity = models.IntegerField(default=1)

        def __str__(self):
            return f"{self.quantity} of {self.item.name}"
        
        # returns the total price value of each product item
        def get_total_item_price(self):
            return self.quantity * self.item.price
        
        # returns the total price value of each product item based on discounted prices
        def get_discount_item_price(self):
            return self.quantity * self.item.discount_price
        
        # returns the value of the price saved from existing discounts
        def get_amount_saved(self):
            return self.get_total_item_price() - self.get_discount_item_price()
        
        # returns which function is used as a price determinant (whether using the original price or discounted price)
        def get_final_product_price(self):
            if self.item.discount_price:
                return self.get_discount_item_price()
            return self.get_total_item_price()
        


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    # payment = models.OneToOneField(Payment, on_delete=models.PROTECT, null=True)
    # cart = models.OneToOneField(Cart, on_delete=models.CASCADE, null=True)
    # customer = models.OneToOneField(Customer, on_delete=models.CASCADE, null=True)
    # logistics = models.ManyToManyField(Delivery)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)

    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    order_number = models.IntegerField()
    order_total = models.IntegerField()
    customer = models.CharField(max_length=32)
    delivery_location = models.CharField(max_length=100)
    payment_options = models.CharField(max_length=100)
    start_date = models.DateTimeField(default=None)
    ordered_date = models.DateTimeField(null=False, default=None)
    
    def __str__(self):
        return self.user
    


