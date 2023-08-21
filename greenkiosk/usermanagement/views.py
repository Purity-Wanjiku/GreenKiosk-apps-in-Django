from django.shortcuts import render, redirect
from .forms import CustomerUploadForm
from .models import Customer

# Create your views here.

def sign_up(request):
    if  request.method == 'POST':
       form = CustomerUploadForm(request.POST, request.FILES)
       if form.is_valid():
        form.save()
    else:
       form = CustomerUploadForm()

    return render (request, 'customer/sign_up.html', {"form" : form})