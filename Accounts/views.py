from django.shortcuts import render,redirect
from .models import *
from .forms import OrderForm
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
     form = OrderForm()
     # ------Condition test send POST data
     if request.method == 'POST':
     #      print("send POST method", request.POST)
          form = OrderForm(request.POST)

          if form.is_valid():
               # ----Save in database
               form.save()
               return redirect('/')

     context = {
          'form': form,
     }
     return render(request,'Accounts/order_form.html', context)


def updateOrder(request, pk):
     order = Order.objects.get(id=pk)
# ---get date to form by use (instance)
     form = OrderForm(instance=order)
# ------Condition test send POST update data
     if request.method == 'POST':
          form = OrderForm(request.POST, instance=order)

          if form.is_valid():
               # ----Save in database
               form.save()
               return redirect('/')
     context = {
          'form': form,
     }
     return render(request,'Accounts/order_form.html', context)

def deleteOrder(request, pk):
     order = Order.objects.get(id=pk)
     if request.method == 'POST':
          order.delete()
          return redirect('/')
     
     context ={
          'item': order
     }
     return render(request,'Accounts/delete.html', context)
