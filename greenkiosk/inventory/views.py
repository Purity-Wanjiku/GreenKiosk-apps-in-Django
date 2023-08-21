from django.shortcuts import render, redirect
from .forms import ProductUploadForm
from .searchform import ProductSearchForm
from .models import Product

# Create your views here.
def upload_product(request):
    if  request.method == 'POST':
      form = ProductUploadForm(request.POST , request.FILES)
      if form.is_valid():
       form.save()
      
    else:
       
       form = ProductUploadForm()
    return render(request, 'inventory/product-upload.html', {"form" : form})

def product_list(request):
    products = Product.objects.all()
    return render(request , "inventory/product_list.html", {"products" : products})


def product_details (request, id):
    product = Product.objects.get( id = id)

    return render(
        request, "inventory/product_detail.html", {"product" : product}
    )


def edit_product(request,id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
       form = ProductUploadForm(request.POST, instance=product)
       if form.is_valid():
          form.save()
          return redirect("product_detail_view", id=id)
    else:
       form = ProductUploadForm(instance=product)

    return render (request, "inventory/product_edit.html", {"form":form})

   
def search(request):
    form = ProductSearchForm(request.GET)
    products = []

    if form.is_valid():
        query = form.cleaned_data.get('query')
        products = Product.objects.filter(name__icontains=query) if query else []

    context = {
        'form': form,
        'products': products,
    }

    return render(request, 'search/search_results.html', context)