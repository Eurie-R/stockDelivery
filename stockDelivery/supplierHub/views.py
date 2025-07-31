from django.shortcuts import render, get_object_or_404, redirect
from .models import Supplier, Product, Order
from .forms import OrderForm, SupplierForm, RestaurantForm, ProductForm, ProductSuppliedForm, AddExistingProductsForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

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

@login_required
def productlist(request):
    # Logic to retrieve and display the list of products
    products = Product.objects.all()  # Assuming you have a Product model
    ctx = {'products': products}
    return render(request, 'productlist.html', ctx)

#TODO 
#Add autentication and authorization to restrict access to the order form
#Fix the order form to only show products that the supplier can supply
#Add to Cart 
#if restaurant is logged in, automatically fill in the restaurant field in the order form
#Order form is only for the supplier 
#Filter the suppliers based on the product 
# This function handles the order form submission

@login_required
def orderform(request):
    if request.method == 'POST':
        # Handle form submission logic here
        orderform = OrderForm(request.POST)
        if orderform.is_valid():
            order = orderform.save()
            order.save()
            return redirect('cart')  # Redirect to cart or another page after successful order
    else:
        orderform = OrderForm(request.POST)
    ctx = {'orderform': orderform}
    return render(request, 'orderform.html', ctx)

@login_required
def getSuppliersForProduct(request, product_id):
    # Logic to retrieve suppliers for a specific product
    product = get_object_or_404(Product, id=product_id)
    suppliers = product.suppliers.filter(product_supplied=product)  # Assuming a ManyToMany relationship with Supplier
    ctx = {'product': product, 'suppliers': suppliers}
    return render(request, 'product_supplierlist.html', ctx)

@login_required
def cart(request):
    order = Order.objects.filter(restaurant=request.user)
    total = sum(order.quantity * order.product.price for order in order)
    ctx =  {'orders': order, 'total': total}
    return render(request, 'cart.html', ctx)

#function that allows a supplier to add a product in their inventory

def addProductToSupplier(request):
    try:
        supplier = Supplier.objects.get(pk=request.user.pk)
    except Supplier.DoesNotExist:
        return HttpResponseForbidden("You are not authorized to add products.")

    if request.method == 'POST':
        productForm = ProductForm(request.POST)
        if productForm.is_valid():
            # Save the product and associate it with the supplier
            product = productForm.save()
            supplier.save()
            supplier.product_supplied.add(product)  # Assuming request.user is a Supplier instance
            return redirect('productlist')  # Redirect to product list after successful addition
    else:
        productForm = ProductForm()

    ctx = {'productForm': productForm}
    return render(request, 'addProduct.html', ctx)  # Render the add product template

def add_existing_products_to_supplier(request):
    try:
        supplier = Supplier.objects.get(pk=request.user.pk)
    except Supplier.DoesNotExist:
        return HttpResponseForbidden("You are not authorized to add products.")

    if request.method == 'POST':
        addform = AddExistingProductsForm(request.POST)
        if addform.is_valid():
            products = addform.cleaned_data['products']
            supplier.product_supplied.add(*products)  # Add selected products to the supplier
            return redirect('productlist')
    else:
        addform = AddExistingProductsForm()

    ctx = {'addform': addform}
    return render(request, 'add_existing_products.html', ctx)


def signup(request):
    # Logic for user signup
    if request.method == 'POST':
        # Handle signup form submission
        supplierForm = SupplierForm(request.POST)
        if supplierForm.is_valid():
            supplier = supplierForm.save(commit=False)
            supplier.user_type = 'SUPPLIER'
            supplier.save()
            return redirect('login')  # Redirect to login or another page after successful signup
    else:
        supplierForm = SupplierForm()
    ctx = {'supplierForm': supplierForm}
    return render(request, 'registration/signup.html',ctx)  # Render the signup template

def restoSignUp(request):
    # Logic for restaurant signup
    if request.method == 'POST':
        # Handle signup form submission
        restoForm = RestaurantForm(request.POST)
        if restoForm.is_valid():
            resto = restoForm.save(commit=False)
            resto.user_type = 'RESTAURANT'
            resto.save()
            return redirect('login')
    else:
        restoForm = RestaurantForm()
    ctx = {'restoForm': restoForm}
    return render(request, 'registration/restoSignUp.html', ctx)  # Render the restaurant signup template