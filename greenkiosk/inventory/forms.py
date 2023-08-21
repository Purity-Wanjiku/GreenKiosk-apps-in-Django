from django import forms
from .models import Product
from django.forms import TextInput, EmailInput

class ProductUploadForm(forms.ModelForm):

    class Meta:  
        model = Product
        fields = "__all__"



