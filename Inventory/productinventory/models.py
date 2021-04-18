from django.db import models

# Create your models here.
class brand(models.Model):
    brand_name=models.CharField(max_length=100)
    available =models.BooleanField(default=False)

    def __str__(self):
        return self.brand_name

class product(models.Model):
    name = models.CharField(max_length=100)
    brand= models.ForeignKey(brand,on_delete=models.SET_NULL,blank=True ,null=True)
    rate= models.CharField(max_length=50)
    available = models.BooleanField(default=False)
    stock = models.CharField(max_length=50,default=0, blank=True,null=True)

    def __str__(self):
        return self.name