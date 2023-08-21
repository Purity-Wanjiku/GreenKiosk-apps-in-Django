from django.shortcuts import render, redirect
from .forms import CartUploadForm
from cartsystem.models import Cart
from orders.models import Order
from inventory.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def upload_cart(request):
    if request.method == 'POST':
       form = CartUploadForm(request.POST, request.FILES)
       if form.is_valid():
         form.save()
    else:
           form = CartUploadForm()
    return render (request, 'cartsystem/cart_upload.html', {"form" : form})

def cart_list(request):
    carts = Cart.objects.all()
    return render( request , "cartsystem/cart_list.html" , {"carts" : carts})

def cart_details(request, id):
    cart = Cart.objects.get(id = id)

    return render(
        request  ,"cartsystem/cart_detail.html",{"cart": cart }
    )


def edit_cart(request,id):
    cart = Cart.objects.get(id=id)

    if request.method == 'POST':
       form =  CartUploadForm(request.POST, instance=cart)
       if form.is_valid():
          form.save()
          return redirect("cart_details", id=id)
    else:
       form = CartUploadForm(instance=cart)

    return render (request, "inventory/cart_edit.html", {"form":form})
        