from django import forms
from .models import Product, Order, Supplier, Restaurant
from django.contrib.auth.forms import UserCreationForm
class OrderForm(forms.ModelForm):
   class Meta:
        model = Order
        fields = '__all__'

class SupplierForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Supplier
        fields = UserCreationForm.Meta.fields + ('username', 'email', 'phone', 'address', 'city', 'state', 'zip_code', 'company_name')
        widgets = {
            'password': forms.PasswordInput(),
        }

class RestaurantForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Restaurant
        fields = UserCreationForm.Meta.fields + ('username', 'email', 'phone', 'address', 'city', 'state', 'zip_code', 'restaurant_name')
        widgets = {
            'password': forms.PasswordInput(),
        }
   