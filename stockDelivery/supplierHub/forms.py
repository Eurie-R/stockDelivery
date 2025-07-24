from django import forms
from .models import Product, Order, Supplier

class OrderForm(forms.ModelForm):
   class Meta:
        model = Order
        fields = '__all__'
   