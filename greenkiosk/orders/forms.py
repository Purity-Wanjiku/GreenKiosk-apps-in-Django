from django import forms
from .models import Order, OrderItem

class OrderUploadForm(forms.ModelForm):

    class Meta:  
        model = Order
        fields = "__all__"

class Meta:  
        model = OrderItem
        fields = "__all__"