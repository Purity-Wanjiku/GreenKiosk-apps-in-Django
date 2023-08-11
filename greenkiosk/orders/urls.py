from django.urls import path
from .views import upload_order, order_details, order_list, edit_order

urlpatterns = [
    path('orders/upload', upload_order, name='order_upload_view'),
    path('orders/list', order_list, name='order_list_view'),
    path('orders/<int:id>/', order_details, name='order_detail_view'),
    path('orders/edit/<int:id>' , edit_order, name='order_edit_view'),
]