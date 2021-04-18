from django.shortcuts import render, redirect
from order.models import order
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import user_logged_in
from productinventory.models import product,brand
from django.contrib import messages

# Create your views here.
def addorder(request):
    if request.method =='POST':
        brand_name= request.POST['brandname']
        product_name=request.POST['productname']
        quantity=request.POST['quantity']
        total_amount=request.POST['total_amount']
        address=request.POST['address']
        pincode=request.POST['pincode']
        email=request.user.email

        # product_name=product.objects.get(id=product_name)


        add_order=order.objects.create(product_name=product.objects.get(id=product_name),brand_name=brand.objects.get(id=brand_name),quantity=quantity,amount_paid=total_amount,address=address,pin_code=pincode,email_by=email)
        add_order.save();
        print('order added')
        messages.info(request,"Order Added Successfully!")
        return redirect('/dashboard')

    else:
        brands=brand.objects.all()
        products=product.objects.all()
        return render(request,'add order.html',{'products':products,'brands':brands})