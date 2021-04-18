from django.db import models
from productinventory.models import *

# Create your models here
# ordername=product.name.append(brand.brand_name)

class order(models.Model):
    # id=models.IntegerField(primary_key=True)
    product_name=models.ForeignKey(product,on_delete=models.PROTECT,blank=False,null=False)
    brand_name=models.ForeignKey(brand,on_delete=models.PROTECT,blank=False,null=False)
    quantity=models.IntegerField()
    amount_paid=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    order_date=models.DateField(auto_now=True)
    pin_code=models.CharField(max_length=10)
    email_by=models.CharField(max_length=150)


    def __str__(self):
        return self.product_name.name