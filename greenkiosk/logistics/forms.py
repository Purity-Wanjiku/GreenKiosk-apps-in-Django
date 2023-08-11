from django import forms
from .models import Delivery

class DeliveryUploadForm(forms.ModelForm):

    class Meta:  
        model = Delivery
        fields = "__all__"