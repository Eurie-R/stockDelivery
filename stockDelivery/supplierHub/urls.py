from django.urls import path
from . import views


urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('supplierlist/', views.supplierlist, name='supplierlist'),
    path('supplierdetail/<int:pk>/', views.supplierdetail, name='supplierdetail'),
    path('productlist/', views.productlist, name='productlist'),
    path('product_suppliers/<int:product_id>/', views.getSuppliersForProduct, name='get_suppliers_for_product'),
    path('orderform/', views.orderform, name='orderform'), 
]

appname = 'supplierHub'
