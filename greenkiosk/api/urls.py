from django.urls import path
from .views import CustomerListView, CustomerDetailView, ProductListView, ProductDetailView

urlpatterns = [
    path("customers/", CustomerListView.as_view(), name="customer_list_view"),
    path("customers/<int:id>/", CustomerDetailView.as_view(), name="customer_detail_view"),
    path("products/", ProductListView.as_view(), name="product_list_view"),
    path("products/<int:id>/", ProductDetailView.as_view(), name= "product_detail_view")
]

