from django.urls import path,include
from . import views

urlpatterns = [
    # path('register',views.createacc,name="register"),
    path('',views.desh,name="home"),
    path('brands',views.brandspage),
    path('products',views.productpage),
    path('orderdetails',views.orderdetails),
    path('dashboard',views.desh),
    path('addorder',include('order.urls'))
    # path('create',views.createacc,name="createuser"),
    # path('login',views.home,name='login'),
]