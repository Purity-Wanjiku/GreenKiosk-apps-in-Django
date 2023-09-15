from rest_framework.views import APIView
from usermanagement.models import Customer
from items.models import Product
from cartsystem.models import Cart
from orders.models import Order
from .serializers import CustomerSerializer, ProductSerializer, CartSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# views that can list customer, create customer, show customer details view, edit customer, delete

class CustomerListView(APIView):
    def get (self , request ):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many = True)  #THIS GETS DATA OF ALL CUSTOMERS IN json FORMAT
        return Response(serializer.data)
    

    def post(self,request):
         serializer = CustomerSerializer(data = request.data)
         #validate the data is in the right format/type
         if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status =  status.HTTP_201_CREATED)
         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class CustomerDetailView(APIView):
    def get(self, request, id, format= None):
        customer= Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        customer = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format = None):
        customer = Customer.objects.get(id=id)
        customer.delete()
        return Response("customer deleted", status=status.HTTP_204_NO_CONTENT)


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True)
        return Response( serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
class ProductDetailView(APIView):
    def get(self, request, id, format=None):
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product,request.data)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def delete (self, request, id, format=None):
        product = Product.objects.get(id=id)
        product.delete()
        return Response("Product is deleted", status=status.HTTP_204_NO_CONTENT)


class OrderListView(APIView):
    def get (self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many = True)
        return Response(request.data)
    
    def post(self, request):
        serializer = OrderSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OrderDetailView(APIView):
    def get(self, request , id, format=None ):
        order = Order.objects.get(id=id)
        serializer = OrderSerializer(order, request.data)
        return Response(serializer.data)
    
    def put(self, request, id, format = None):
        order = Order.objects.get(id=id)
        serializer = OrderSerializer(order, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        order = Order.objects.get(id=id)
        order.delete()
        return Response("Order is deleted", status=status.HTTP_204_NO_CONTENT)



class AddToCartView(APIView):
    def post(self, request,id, format = None):
        cart_id = request.data["cart_id"]
        product_id = request.data["product_id"]
        cart = Cart.objects.get(id = cart_id)
        product = Product.get(id = product_id)
        updated_cart = cart.add_product(product)
        serializer = CartSerializer(updated_cart)
        return Response(serializer.data)
    





