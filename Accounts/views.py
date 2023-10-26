from django.shortcuts import render,redirect
from .models import *
from .forms import OrderForm, CreateUserForm, CustomerForm
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_user,admin_only
from django.contrib.auth.models import Group
# Create your views here.


#======Register page========
def registerPage(request):
     # -----can't access to register page again when you already log-------
     if request.user.is_authenticated:
          return redirect('home')
     
     else:
          form = CreateUserForm()
          if request.method == 'POST':
               form = CreateUserForm(request.POST)
               if form.is_valid():
                    user = form.save()
                    group = Group.objects.get(name='customer')
                    user.groups.add(group)
                    Customer.objects.create(user=user)
                    username = form.cleaned_data.get('username')
                    messages.success(request, f'Account was created for {username}')
                    return redirect('login')

     context = {
          'form': form,
     }
     return render(request,'Accounts/register.html', context)


# =========== Login page=========================================================
#------ចាប់ paramter---    
@unauthenticated_user
def loginPage(request):
     # -----can't access to login page again when you already log-------
     # if request.user.is_authenticated:
     #      return redirect('home')
     
     # else:
          if request.method == 'POST':
               username = request.POST.get('username')
               password = request.POST.get('password')
               user = authenticate(request, username= username, password= password)
          # if user is not None:
               login(request, user)
               return redirect('home')
          # else:
          #      messages.info(request, f'Wrong Username or Password')

          context = {

          }

          return render(request,'Accounts/login.html', context)

# =========Logout page===============================================================
def logoutUser(request):
     logout(request)
     return redirect('login')

# ======User Page ===================================================================
@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def userPage(request):
     orders = request.user.customer.order_set.all()
     total_orders = orders.count()
     delivered = orders.filter(status='Delivered').count()
     pending = orders.filter(status='Pending').count()
     context ={
          'orders': orders,
          'total_orders': total_orders,
          'delivered': delivered,
          'pending': pending,
     }

     return render(request,'Accounts/user.html', context)


#======Home Page ===================================================================
# -close page when logout--- 
@login_required(login_url='login')
@admin_only
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


# ======Product page============================================================
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def products(request):
     products = Product.objects.all()
     
     return render(request,'Accounts/products.html', {'products': products})



#======Account setting ======================================================
@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def accountSettings(request):
     customer = request.user.customer
     form = CustomerForm(instance=customer)

     if  request.method == 'POST':
          form = CustomerForm(request.POST, request.FILES, instance=customer)
          if form.is_valid():
               form.save()

     context ={
          'form': form,
     }

     return render(request, 'Accounts/account_settings.html', context)


# =====Customer page===============================================================
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def customer(request, pk):
     customers = Customer.objects.get(id=pk)
     orders = customers.order_set.all()
     total_orders = orders.count()

     myFilter = OrderFilter(request.GET, queryset=orders)
     orders = myFilter.qs

     context = {
          'myFilter': myFilter,
          'customers': customers,
          'orders': orders,
          'total_orders': total_orders,
     }
     return render(request,'Accounts/customer.html', context)

# ========Create Order===============
@allowed_user(allowed_roles=['admin'])
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

@allowed_user(allowed_roles=['admin'])
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

@allowed_user(allowed_roles=['admin'])
def deleteOrder(request, pk):
     order = Order.objects.get(id=pk)
     if request.method == 'POST':
          order.delete()
          return redirect('/')
     
     context ={
          'item': order
     }
     return render(request,'Accounts/delete.html', context)
