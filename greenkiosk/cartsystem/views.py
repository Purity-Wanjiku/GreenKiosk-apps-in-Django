from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CartUploadForm
from cartsystem.models import Cart
from orders.models import Order
from items.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required
def upload_cart(request):
    if request.method == 'POST':
       form = CartUploadForm(request.POST, request.FILES)
       if form.is_valid():
         user = request.user
         cart, created = Cart.objects.get_or_create(user=user, defaults={
            'quantity': 0,
            'product_price': 0.0,
            'payment_method': "",
            'delivery_cost': 0.0   
         })
         messages.success(request, 'Cart updated successfully.')
         return redirect('cart_list')
       form.save()
    else:
           form = CartUploadForm()
    return render (request, 'cartsystem/cart_upload.html', {"form" : form})


@login_required
def cart_list(request):
    carts = Cart.objects.all()
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user, defaults={
            'quantity': 0,
            'product_price': 0.0,
            'payment_method': "",
            'delivery_cost': 0.0   
         })
    messages.success(request, 'Cart updated successfully.')

    return render( request , "cartsystem/cart_list.html" , {"carts" : carts})


@login_required
def cart_details(request, id):
    cart = Cart.objects.get(id = id)

    user = request.user
    cart, created = Cart.objects.get_or_create(user=user, defaults={
            'quantity': 0,
            'product_price': 0.0,
            'payment_method': "",
            'delivery_cost': 0.0   
         })
    messages.success(request, 'Cart updated successfully.')

    return render(
        request  ,"cartsystem/cart_detail.html",{"cart": cart }
    )

@login_required
def edit_cart(request,id):
    cart = Cart.objects.get(id=id)

    user = request.user
    try:
        cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        cart = None

    if request.method == 'POST':
       form =  CartUploadForm(request.POST, instance=cart)
       if form.is_valid():
          form.save()
          return redirect("cart_details", id=id)
    else:
       form = CartUploadForm(instance=cart)

    return render (request, "inventory/cart_edit.html", {"form":form})


        