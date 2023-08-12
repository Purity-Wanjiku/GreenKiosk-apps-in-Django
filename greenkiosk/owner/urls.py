from django.urls import path
from .views import upload_vendor, vendor_list, vendor_details, edit_vendor


urlpatterns = [
   path('vendor/upload', upload_vendor, name='vendor_upload_view'),
   path('vendor/list', vendor_list, name= 'vendor_list_view'),
    path('vendor/<int:id>/', vendor_details, name='vendor_detail_view'),
    path('vendor/edit/<int:id>' , edit_vendor, name='vendor_edit_view'),
]