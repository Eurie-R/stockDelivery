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
    #This supplier supplies these products    
    product_supplied = models.ManyToManyField('Product', related_name='suppliers')

    def __str__(self):
        return self.company_name
    
class Restaurant(CustomUser):
    restaurant_name = models.CharField(max_length=255, blank=False)
    
    def __str__(self):
        return self.restaurant_name

#Product can have multiple suppliers that can supply it
class Product(models.Model):
    #supplier = models.ManyToManyField(Supplier, related_name='products')
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    #related name is how you can access the orders from the supplier and restaurant
    #e.g. supplier.orders.all() or restaurant.orders.all()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='orders')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    arrival_date = models.DateTimeField()

    def __str__(self):
        return f"Order {self.id} - {self.product.name} for {self.restaurant.restaurant_name}"