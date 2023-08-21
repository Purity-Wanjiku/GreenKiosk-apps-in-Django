from django.urls import path
from .views import sign_up

urlpatterns = [
    path('customer/upload', sign_up, name='sign_up_view')
]