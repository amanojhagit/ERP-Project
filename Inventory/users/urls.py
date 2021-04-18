from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('register',views.createacc,name="register"),
    path('',views.home,name="home"),
    # path('create',views.createacc,name="createuser"),
    path('login',views.home,name='login'),
    path('logout',views.logout),
]