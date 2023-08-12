from django.shortcuts import render, redirect
from .forms import VendorUploadForm
from owner.models import Vendor

# Create your views here.
def upload_vendor(request):
    if  request.method == 'POST':
      form = VendorUploadForm(request.POST , request.FILES)
      if form.is_valid():
       form.save()
      
    else:
       
       form = VendorUploadForm()
    return render(request, 'owner/owner_upload.html', {"form" : form})

def vendor_list(request):
    vendors = Vendor.objects.all()

    return render(request , "owner/owner_list.html", {"vendors" : vendors})

def vendor_details (request, id):
    vendor = Vendor.objects.get( id = id)

    return render(
        request, "owner/owner_detail.html", {"vendor" : vendor}
    )


def edit_vendor(request,id):
    vendor = Vendor.objects.get(id=id)

    if request.method == 'POST':
       form = VendorUploadForm(request.POST, instance=vendor)
       if form.is_valid():
          form.save()
          return redirect("owner_details", id=id)
    else:
       form = VendorUploadForm(instance=product)

    return render (request, "owner/owner_edit.html", {"form":form})
