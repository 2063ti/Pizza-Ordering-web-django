from django.db import models

# Create your models here.

class User(models.Model):
    User_id  = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact =  models.CharField(max_length=13)
    email_id = models.EmailField(unique=True)
    password = models.CharField(max_length=9)
    gender = models.CharField(max_length=1)
    otp = models.CharField(max_length=10)
    otp_used = models.IntegerField()
    is_admin = models.IntegerField()

    class Meta:
        db_table = 'User'

class Pizza_type(models.Model):
    Pizza_type_id  = models.AutoField(primary_key=True)
    Pizza_type_name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    class Meta:
        db_table = 'Pizza_type'
        
class Offer(models.Model):
    Offers_id  = models.AutoField(primary_key=True)
    Offers_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    Start_Date = models.DateField()
    End_Date = models.DateField()
    coupon_code = models.CharField(max_length=30)
    Discount = models.DecimalField(max_digits=5,decimal_places=2)

    class Meta:
        db_table = 'Offer'

class Pizza_Menu(models.Model):
    Pizza_menu_id = models.AutoField(primary_key=True)
    Pizza_Name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    Pizza_type_id = models.ForeignKey(Pizza_type,on_delete=models.CASCADE)
    Offers_id = models.ForeignKey(Offer,on_delete=models.CASCADE)
    Reg_serve_price = models.IntegerField()
    med_serve_price = models.IntegerField()
    lar_serve_price = models.IntegerField()

    class Meta:
        db_table = 'Pizza_Menu'

class Delivery_Boy(models.Model):
    delivery_boy_id = models.AutoField(primary_key=True)
    Delivery_boy_Name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10)
    is_available = models.CharField(max_length=5)
    class Meta:
        db_table = 'Delivery'


class order(models.Model):
    order_id  = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    order_date = models.DateField()
    delivery_address = models.CharField(max_length=50)
    Total_amount =  models.IntegerField()
    order_status = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=20)
    payment_mode = models.CharField(max_length=20)
    delivery_status = models.CharField(max_length=30)
    delivery_boy_id = models.ForeignKey(Delivery_Boy,on_delete=models.CASCADE)
    class Meta:
        db_table = 'order'


class order_Items(models.Model):
    order_de_id  = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(order,on_delete=models.CASCADE)
    pizza_menu_id = models.ForeignKey(Pizza_Menu,on_delete=models.CASCADE)
    Quantity = models.CharField(max_length=50)
    subtotal = models.CharField(max_length=50)

    class Meta:
        db_table = 'order_De'

class Cart(models.Model):
    Cart_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    Pizza_Menu_id = models.ForeignKey(Pizza_Menu,on_delete=models.CASCADE)
    amount = models.IntegerField()
    Quantity = models.IntegerField()
    date = models.DateField()

    class Meta:
        db_table = 'cart'
    


class Table(models.Model):
    table_id = models.AutoField(primary_key=True)
    table_no = models.IntegerField()
    capacity = models.IntegerField()
    layout = models.IntegerField()
    charges = models.IntegerField()

    class Meta:
        db_table = 'Table'


class Table_book(models.Model):
    Booking_id  = models.AutoField(primary_key=True)
    table_id = models.ForeignKey(Table,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    Booking_Date = models.DateTimeField()
    Booking_Time = models.DateTimeField()
    code = models.CharField(max_length=30)
    Booking_Status = models.CharField(max_length=50)

    class Meta:
        db_table = 'Table_book'

class Feedback(models.Model):
    Feedback_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    Pizza_Menu_id = models.ForeignKey(Pizza_Menu,on_delete=models.CASCADE)
    Feedback_date = models.DateField()
    rating = models.IntegerField()
    comments = models.CharField(max_length=200)

    class Meta:
        db_table = 'Feedback'