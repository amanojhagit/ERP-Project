from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.addorder,name="add order"),
    # path('addorder',views.addorder),
    # path('',views.home,name="home"),
    # path('create',views.createacc,name="createuser"),
    # path('login',views.home,name='home'),
]
