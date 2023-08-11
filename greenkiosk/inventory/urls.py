from django.urls import path
from .views import upload_product,product_list,product_details, edit_product

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('products/upload', upload_product, name='product_upload_view'),
    path("products/list",product_list,name= "product_list_view"),
    path("products/<int:id>/", product_details, name="product_detail_view"),
    path("products/edit/<int:id>", edit_product, name="product_edit_view"),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
