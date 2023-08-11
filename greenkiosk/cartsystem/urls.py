from django.urls import path
from .views import upload_cart, cart_list, cart_details, edit_cart

urlpatterns = [
    path ('carts/upload', upload_cart, name= 'cart_upload_view'),
    path('carts/list', cart_list, name='cart_list_view'),
    path('carts/<int:id>/',cart_details, name='cart_detail_view'),
    path("carts/edit/<int:id>",edit_cart , name="cart_edit_view"),
    ]