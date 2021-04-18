from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
# from .models import customuser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User,auth
from django.contrib import messages
import re

# Create your views here.
# @csrf_exempt

# def sigin(request):



def createacc(request):
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        # mobile=request.POST['mobile']
        user_name=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                print('Username Taken')
                messages.info(request,'Phone number already registered')
                return redirect('/register')
            if User.objects.filter(email=email).exists():
                print('Email already exists.')
                messages.info(request,"Email already registered")
                return redirect('/register')
            else:
                user=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=user_name,password=password1)
                user.save();
                print('User Created')
        else:
            print("Password did'nt match")
            messages.info(request,"Password did not matched")
            return redirect('/register')
        return redirect('/')
        
    else:
        return render(request,'NewAccount.html')

def home(request):
    if request.method == 'POST':
        username=request.POST['email']
        password=request.POST['password']

        # user=auth.authenticate(request,username=email,password=password)
        
        # if user is not None:
        #     auth.login(request,user)
        #     messages.info(request,'User Logged In')
        #     return redirect('login')
        # else:
        #     messages.info(request,'Invalid Credentials')
        #     return redirect('login')


#validation part

        if not re.match("^[\w\.\+\@[\w]+\.[a-z]{2,3}$", username):
            messages.info(request,'Enter valid Email')
            return redirect('login')
            # return JsonResponse({'error':'Enter a valid email'})
    

        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(email=username)
        
            if user.check_password(password):
                auth.login(request,user)
                # messages.info(request,'User Logged In')
                return redirect('/dashboard')
        
            else:
                messages.info(request,'Invalid Password')
                return redirect('login')


        except UserModel.DoesNotExist:
            messages.info(request,'Invalid Email')
            return redirect('login')

    else:
        return render(request,'Login.html')

def logout(request):
    auth.logout(request)
    messages.info(request,'User Logged Out')
    return redirect('login')