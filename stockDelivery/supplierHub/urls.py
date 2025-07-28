from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('supplierlist/', views.supplierlist, name='supplierlist'),
    path('supplierdetail/<int:pk>/', views.supplierdetail, name='supplierdetail'),
    path('productlist/', views.productlist, name='productlist'),
    path('product_suppliers/<int:product_id>/', views.getSuppliersForProduct, name='get_suppliers_for_product'),
    path('orderform/', views.orderform, name='orderform'), 
    path('signup/', views.signup, name='signup'),  
    path('restosignup/', views.restoSignUp, name='restosignup'), 
    path('cart/', views.cart, name='cart'),
    #path('checkout/', views.checkout, name='checkout'),



    # Password Reset URLs
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'registration/password_reset.html'), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = 'registration/password_reset_sent.html'), name='password_reset_done'),
    path('reset_/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'registration/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'registration/password_reset_done.html'), name='password_reset_complete'),

]

appname = 'supplierHub'

