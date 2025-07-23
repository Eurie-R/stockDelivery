from django.shortcuts import render
from .models import Supplier

def landingpage(request):
    return render(request, 'landingpage.html')

def supplierlist(request):
    # Logic to retrieve and display the list of suppliers
    suppliers = Supplier.objects.all()  # Assuming you have a Supplier model
    ctx = {'suppliers': suppliers}
    return render(request, 'supplierlist.html',ctx)

def supplierdetail(request, supplier_id):
    # Logic to retrieve and display details of a specific supplier
    supplier = Supplier.objects.get(id=supplier_id)
    ctx = {'supplier': supplier}
    return render(request, 'supplierdetail.html', ctx)