from django.shortcuts import render
from .forms import CartUploadForm
# Create your views here.

def upload_cart(request):
    form = CartUploadForm()
    return render (request, 'cartsystem/cart-upload.html', {"form" : form})
