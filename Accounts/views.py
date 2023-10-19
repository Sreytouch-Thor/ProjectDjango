from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
         'customers': customers,
         'orders' : orders,
         'total_customers': total_customers,
         'total_orders': total_orders,
         'delivered': delivered,
         'pending': pending,
    }
    return render(request,'Accounts/dashboard.html', context)

def products(request):
     products = Product.objects.all()
     
     return render(request,'Accounts/products.html', {'products': products})

def customer(request, pk):
     customers = Customer.objects.get(id=pk)
     orders = customers.order_set.all()
     total_orders = orders.count()

     context = {
          'customers': customers,
          'orders': orders,
          'total_orders': total_orders,
     }
     return render(request,'Accounts/customer.html', context)

def createOrder(request):

     return render(request,'Accounts/order_form.html')