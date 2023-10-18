from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    context = {
         'customers': customers,
         'orders' : orders,
    }
    return render(request,'Accounts/dashboard.html', context)

def products(request):
     products = Product.objects.all()
     
     return render(request,'Accounts/products.html', {'products': products})

def customer(request):
     return render(request,'Accounts/customer.html')
