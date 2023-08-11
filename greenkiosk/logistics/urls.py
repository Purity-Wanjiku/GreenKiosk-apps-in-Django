from django.urls import path
from .views import upload_delivery, delivery_details, edit_delivery, delivery_list

urlpatterns = [
    path('logistics/upload/', upload_delivery, name='delivery_upload_view'),
    path("logistics/list/",delivery_list,name= "delivery_list_view"),
    path("logistics/<int:id>/", delivery_details, name="delivery_detail_view"),
    path("logistics/edit/<int:id>/", edit_delivery, name="delivery_edit_view"),

]