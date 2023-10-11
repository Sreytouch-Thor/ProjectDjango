from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'Accounts/dashboard.html')

def products(request):
     return render(request,'Accounts/products.html')
def customer(request):
     return render(request,'Accounts/customer.html')
