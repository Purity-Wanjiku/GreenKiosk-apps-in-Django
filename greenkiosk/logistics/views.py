from django.shortcuts import render, redirect
from .forms import DeliveryUploadForm
from logistics.models import Delivery
# Create your views here.

def upload_delivery(request):
    if request.method == 'POST':
        form = DeliveryUploadForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=DeliveryUploadForm()
    return render (request, 'logistics/logistics_upload.html', {'form' : form})

def delivery_list(request):
    delivery = Delivery.objects.all()

    return render( 
       request , "logistics/logistics_list.html", {"delivery" : delivery}
    )

def delivery_details (request, id):
    delivery = Delivery.objects.get( id = id)

    return render(
        request, "logistics/logistics_detail.html", {"delivery" : delivery}
    )

def edit_delivery(request,id):
    delivery = Delivery.objects.get(id=id)

    if request.method == 'POST':
       form = DeliveryUploadForm(request.POST, instance=delivery)
       if form.is_valid():
          form.save()
          return redirect("delivery_details", id=id)
    else:
       form = DeliveryUploadForm(instance=delivery)

    return render (request, "logistics/logistics_edit.html", {"form":form})
