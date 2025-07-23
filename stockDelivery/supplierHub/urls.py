from django.urls import path
from . import views


urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('supplierlist/', views.supplierlist, name='supplierlist'),
]

appname = 'supplierHub'
