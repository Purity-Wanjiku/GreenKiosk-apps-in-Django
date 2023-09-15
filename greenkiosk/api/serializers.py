# it serializes the data from json to model fields
    # """Serializers a customer object into JSON format."""

from rest_framework import serializers
from usermanagement.models import Customer
from items.models import Product
from cartsystem.models import Cart
from orders.models import Order



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many = True)

    class Meta:
        model=Cart
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"