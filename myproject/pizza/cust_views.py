import json
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import auth
from .models import *
from .forms import UserProfileForm
from .forms import *
from django import forms
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from cart.cart import Cart
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

@login_required
def booking(request):
    return render(request,"booking.html")

def services(request):
    return render(request,"service.html")

def menu(request):
    products=Pizza_Menu.objects.all()
    return render(request,"menu.html",{"products":products})

def contact(request):
    return render(request,"contact.html")

def registration(request):
    try :
        if request.method == 'POST':
         
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            password1=request.POST['password1']
            password2=request.POST['password2']
            email=request.POST['email']
            contact=request.POST['contact']
            gender=request.POST['gender']
            if password1==password2:
                if CustomUser.objects.filter(email=email).exists():
                    messages.info(request,'email taken')
                    return redirect('registration')
                else:
                    user = CustomUser.objects.create_user(email=email, password=password1, first_name=first_name, 
                            last_name=last_name,contact=contact,gender=gender)
                    user.save()
                    print('user created')
                    return redirect('log')
            else:
                messages.info(request,'password not mathching.....')
                return redirect('registration')
            
        else:
            
            return render(request,"registration.html")
    except Exception as e :
        print(e)
        return HttpResponse("something Went Wrong ",e)

def log(request):
    try:
        if request.method=='POST':
            
            email=request.POST['email']
            password=request.POST['password']
            
            user = auth.authenticate(request,email=email,password=password)
            
            # if user is not None:
            #     auth.login(request,user)
            #     return redirect("/")
            if user is not None:
                    print("h")
                    auth.login(request,user)



                    # Do some shopping cart stuff
                    current_user = CustomUser.objects.get(id=request.user.id)
			        # Get their saved cart from database
                    saved_cart = current_user.old_cart
			        # Convert database string to python dictionary
                    if saved_cart:
				    # Convert to dictionary using JSON
                        converted_cart = json.loads(saved_cart)
				    # Add the loaded cart dictionary to our session
				    # Get the cart
                        cart = Cart(request)
				        # Loop thru the cart and add the items from the database
                        for key,value in converted_cart.items():
                            #  print("key:",key,"values:",value)
                             cart.db_add(product=key, price=int(value["price"]),quantity=int(value["Quantity"]))


                    messages.info(request,"You Have Been Loged In Successfully...")
                    return redirect("/")
            else:
                print(user)
                print(f"Authentication failed for username: {email}")
                print("h1")
                messages.info(request,"invalid credentials")
                return redirect("log")
        else: 
            print("h2")
            return render(request,"login1.html")
        
    except Exception as e:
        print(e)
        return HttpResponse('Error occurred') 
    
def logout(request):
    auth.logout(request)
    return redirect('/')
    

def forgot(request):
    return render(request,"forget.html")

@login_required
def p_view(request):
    if request.user.is_authenticated:
        puser= CustomUser.objects.get(id=request.user.id)
        return render(request,"p_view.html",{'puser':puser})


def contact(request,):

    
    if request.method=='POST':
        name=request.POST['name']
        subject=request.POST['subject']
        email=request.POST['email']
        msg=request.POST['message']
        contact = ContactUs.objects.create(
            name=name,
            email=email,
            subject=subject,
            msg=msg)
        send_mail(
            subject,#subject
            msg,#message
            email,#from email
            ['tirth5524@gmail.com']# to email
        )
        return render(request,'contact.html',{'name':name})
    else :
        return render(request,'contact.html',{})
@login_required
def feedback(request):

        if request.method=='POST':
            name=request.POST['pname']
            email=request.POST['email']
            msg=request.POST['message']
            rate=request.POST['rating']
            feedback = Feedback.objects.create(
                p_name=name,
                email=email,
                rate=rate,
                message=msg)
            messages.info(request,"You Have Successfuly filled Feedback Form")
            return render(request,'feedback.html',)
        else :
            return render(request,'feedback.html')
        
@login_required
def update_user(request):
    
        # current_user=CustomUser.objects.get(id=request.id)
        if request.method == 'POST':
            form = UserProfileForm(request.POST,request.FILES,instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('/') 
       
        else:
            form = UserProfileForm(instance=request.user)
        return render(request,'update_user.html',{'form':form})

def product(request,pk):
	product = Pizza_Menu.objects.get(Pizza_menu_id=pk)
	return render(request, 'product.html', {'product':product})

@login_required
def payment_success(request):
	return render(request, "payment_success.html", {})

@login_required
def update_info(request):
	if request.user.is_authenticated:
		
		
		# Get Current User's Shipping Info
		shipping_user = ShippingAddress.objects.get(user=request.user.id)
		

		# Get User's Shipping Form
		shipping_form = ShippingForm(request.POST or None, instance=shipping_user)		
		if  shipping_form.is_valid():
			
			# Save shipping form
			shipping_form.save()

			messages.success(request, "Your Info Has Been Updated!!")
			return redirect('indux')
		return render(request, "shippingInfo.html", {'shipping_form':shipping_form})
	else:
		messages.success(request, "You Must Be Logged In To Access That Page!!")
		return redirect('indux')


def checkout(request):
	# Get the cart
	cart = Cart(request)
	cart_products = cart.get_prods
	quantities = cart.get_quants
	totals = cart.cart_total()

	if request.user.is_authenticated:
		# Checkout as logged in user
		# Shipping User
		shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
		# Shipping Form
		shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
		return render(request, "checkout.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form })
	else:
		# Checkout as guest
		shipping_form = ShippingForm(request.POST or None)
		return render(request, "checkout.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form})