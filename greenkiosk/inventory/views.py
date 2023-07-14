from django.shortcuts import render
from .forms import ProductUploadForm

# Create your views here.
def upload_product(request):
    form = ProductUploadForm()
    return render(request, 'inventory/product-upload.html', {"form" : form})

