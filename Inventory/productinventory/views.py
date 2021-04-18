from django.shortcuts import render,redirect
# from django.user.auth import is_authenticated
from django.contrib.auth.models import User,auth
from .models import brand,product
from order.models import order

# Create your views here.
def desh(request):
    # if user.is_authenticated:
    return render(request,'Dashboard.html')
    # else:
        # return redirect('/')

def productpage(request):
    products = product.objects.all()
    return render(request,'products.html',{'products':products})

def brandspage(request):
    brands= brand.objects.all()
    
    return render(request,'brands.html',{'brands':brands})

def orderdetails(request):
    orders = order.objects.all()
    return render(request,'order details.html',{'orders':orders})