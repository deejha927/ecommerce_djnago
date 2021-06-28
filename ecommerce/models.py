from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class register(models.Model):
    user_fname=models.CharField(max_length=30)
    user_lname=models.CharField(max_length=30)
    user_email=models.EmailField(max_length=254)
    user_pass=models.CharField(max_length=50)
    user_contact=models.BigIntegerField(null=True)
    def __str__(self):
        return self.user_email

class customer(models.Model):
    user=models.OneToOneField(register,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name
    

class product(models.Model):
    product_name=models.CharField(max_length=100)
    product_price=models.FloatField()
    product_description=models.CharField(max_length=200)
    product_image=models.ImageField(null=True,blank=True)
    product_image1=models.ImageField(null=True,blank=True)
    product_image2=models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.product_name

class order(models.Model):
    customer=models.ForeignKey(customer,on_delete=models.CASCADE,null=True,blank=True)
    date_order=models.DateField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=True)
    transcation_id=models.CharField(max_length=100,null=True)
    def __str__(self):
        return str(self.id)
    
    @property
    def get_count(self):
        vals=self.orderitem_set.all().count()
        return vals
    @property
    def cart_total(self):
        total=0
        vals=self.orderitem_set.all()
        for item in vals:
            total+=item.get_total 
        return total

    @property
    def cart_items(self):
        vals=self.orderitem_set.all()
        total=sum([item.quantity for item in vals])
        return total

class orderitem(models.Model):
    product=models.ForeignKey(product,on_delete=models.SET_NULL,blank=True,null=True)
    order=models.ForeignKey(order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity=models.IntegerField(default=0,blank=True,null=True)
    added_date=models.DateField(auto_now_add=True)
    
    @property
    def get_total(self):
        ans =self.product.product_price * self.quantity
        return ans

class shipping_details(models.Model):
    customer=models.ForeignKey(customer,on_delete=models.SET_NULL,blank=True,null=True)
    order=models.ForeignKey(order,on_delete=models.SET_NULL,blank=True,null=True)
    address=models.CharField(max_length=500,null=True)
    city=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    zipcode=models.CharField(max_length=50,null=True)
    orderes_date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.address
    