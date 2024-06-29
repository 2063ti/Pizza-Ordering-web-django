from django.db import models
from datetime import date
from django.db import models
from typing import Any
from django.db.models.base import Model as Model
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manage import UserManager
from django.db import models





# Create your models here.

class CustomUser(AbstractUser):
    username=None
    contact =  models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1)
    otp = models.CharField(max_length=10)
    otp_used = models.IntegerField(null=True,blank=True)
    is_admin = models.IntegerField(null=True,blank=True)
    last_login_time=models.DateTimeField(null=True,blank=True)
    last_log_time=models.DateTimeField(null=True,blank=True)
    is_verified=models.BooleanField(default=False)
    email_token=models.CharField(max_length=100,null=True,blank=True)
    forget_password=models.CharField(max_length=100,null=True,blank=True)
    old_cart = models.CharField(max_length=200, blank=True, null=True)

    objects = UserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]



class Pizza_type(models.Model):
    Pizza_type_id  = models.AutoField(primary_key=True)
    Pizza_type_name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

        
# class Offer(models.Model):
#     Offers_id  = models.AutoField(primary_key=True)
#     Offers_name = models.CharField(max_length=50)
#     description = models.CharField(max_length=200)
#     Start_Date = models.DateField()
#     End_Date = models.DateField()
#     coupon_code = models.CharField(max_length=30)
#     Discount = models.DecimalField(max_digits=5,decimal_places=2)

#     class Meta:
#         db_table = 'Offer'

class Pizza_Menu(models.Model):
    Pizza_menu_id = models.AutoField(primary_key=True)
    Pizza_Name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    Pizza_type_id = models.ForeignKey(Pizza_type,on_delete=models.CASCADE)
    is_sale = models.BooleanField(default=False)
    sale_price =  models.IntegerField()
    Reg_serve_price = models.IntegerField()
    med_serve_price = models.IntegerField()
    lar_serve_price = models.IntegerField()
    img = models.ImageField(upload_to='pics/')
  
class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=50)
    msg = models.CharField(max_length=100)

    class Meta:
        db_table = 'contactus'

class Feedback(models.Model):
    
    p_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    rate = models.CharField(max_length=50)
    message = models.CharField(max_length=200)

    class Meta:
        db_table = 'feedback'

import datetime

class order(models.Model):
    order_id  = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    order_date = models.DateField(default=datetime.datetime.today)
    delivery_address = models.CharField(max_length=50)
    order_status = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=20)
    payment_mode = models.CharField(max_length=20)
    delivery_status = models.CharField(max_length=30)
    email = models.EmailField(max_length=250,null=True,blank=True)
    full_name = models.CharField(max_length=250,null=True,blank=True)
    Shipping_address=models.TextField(max_length=1500,null=True)
    amount_paid= models.DecimalField(max_digits=7, decimal_places=2,default=0)

    def __str__(self):
          return f'Order - {str(self.id)}'


class order_Items(models.Model):
    order_de_id  = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    order_id = models.ForeignKey(order,on_delete=models.CASCADE)
    pizza_menu_id = models.ForeignKey(Pizza_Menu,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=7, decimal_places=2,default=0)

    def __str__(self):
          return f'Order Item - {str(self.id)}'

# Customers
class Customer(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone = models.CharField(max_length=10)
	email = models.EmailField(max_length=100)
	password = models.CharField(max_length=100)


	def __str__(self):
		return f'{self.first_name} {self.last_name}'


class ShippingAddress(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
	shipping_full_name = models.CharField(max_length=255)
	shipping_email = models.CharField(max_length=255)
	shipping_address1 = models.CharField(max_length=255)
	shipping_address2 = models.CharField(max_length=255, null=True, blank=True)
	shipping_city = models.CharField(max_length=255)
	shipping_state = models.CharField(max_length=255, null=True, blank=True)
	shipping_zipcode = models.CharField(max_length=255, null=True, blank=True)
	


	# Don't pluralize address
	class Meta:
		verbose_name_plural = "Shipping Address"

	def __str__(self):
		return f'Shipping Address - {str(self.id)}'