from django.contrib import admin
from .models import CustomUser, Supplier, Restaurant, Product, Order
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class SupplierAdmin(admin.ModelAdmin):
    model = Supplier
    list_display = ('company_name', 'user_type', 'phone', 'created_at')
    search_fields = ('company_name', 'user_type')
    list_filter = ('product_supplied',)

class RestaurantAdmin(admin.ModelAdmin):
    model = Restaurant
    list_display = ('restaurant_name', 'user_type', 'phone', 'created_at')
    search_fields = ('restaurant_name', 'user_type')


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'price', 'created_at')
    search_fields = ('name',)

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('restaurant', 'supplier', 'product', 'quantity', 'order_date', 'arrival_date')
    search_fields = ('restaurant',)
 # Unregister the default user model
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
