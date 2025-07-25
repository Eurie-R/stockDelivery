from django.urls import path
from . import views


urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('supplierlist/', views.supplierlist, name='supplierlist'),
    path('supplierdetail/<int:pk>/', views.supplierdetail, name='supplierdetail'),
    path('productlist/', views.productlist, name='productlist'),
    path('product_suppliers/<int:product_id>/', views.getSuppliersForProduct, name='get_suppliers_for_product'),
    path('orderform/', views.orderform, name='orderform'), 
    path('signup/', views.signup, name='signup'),  # Assuming you have a signup view
    path('restosignup/', views.restoSignUp, name='restosignup'),  # Assuming you have a restaurant signup view
]

appname = 'supplierHub'
