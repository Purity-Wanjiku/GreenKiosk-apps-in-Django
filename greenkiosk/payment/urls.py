from django.urls import path
from .views import upload_payment

urlpatterns = [
    path('payment/upload', upload_payment, name="upload_payment_view")
]