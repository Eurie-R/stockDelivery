from django.shortcuts import render, get_object_or_404
from .models import Supplier, Product

def landingpage(request):
    return render(request, 'landingpage.html')

def supplierlist(request):
    # Logic to retrieve and display the list of suppliers
    suppliers = Supplier.objects.all()  # Assuming you have a Supplier model
    ctx = {'suppliers': suppliers}
    return render(request, 'supplierlist.html',ctx)

def supplierdetail(request, pk):
    # Logic to retrieve and display details of a specific supplier
    supplier = get_object_or_404(Supplier, pk=pk)
    products = supplier.product_supplied.all()  # Assuming a ManyToMany relationship with Product
    ctx = {'supplier': supplier, 'products': products}
    return render(request, 'supplierdetail.html', ctx)