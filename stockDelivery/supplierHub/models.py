from django.db import models
from django.contrib.auth.models import AbstractUser

# Basis for the Multi-table inheritance
# CustomUser will be the base class for both Supplier and Restaurant models
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('SUPPLIER', 'Supplier'),
        ('RESTAURANT', 'Restaurant'),
    )

    user_type = models.CharField(blank=False, choices=USER_TYPE_CHOICES)
    phone = models.CharField(blank=True, max_length=255)
    created_at = models.DateField(auto_now_add=True)
    address = models.TextField(blank=False)
    city = models.CharField(max_length=100, blank=False)
    state = models.CharField(max_length=100, blank=False)
    zip_code = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.name

class Supplier(CustomUser):
    company_name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.company_name
    
class Restaurant(CustomUser):
    restaurant_name = models.CharField(max_length=255, blank=False)
    
    def __str__(self):
        return self.restaurant_name

#Product can have multiple suppliers that can supply it
class Product(models.Model):
    supplier = models.ManyToManyField(Supplier, related_name='products')
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name