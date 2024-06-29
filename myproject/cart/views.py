from django.shortcuts import render, get_object_or_404
from .cart import Cart
from pizza.models import *
from django.http import JsonResponse
from django.contrib import messages
import re
def cart_summary(request):
    # Get the cart
	cart = Cart(request)
	cart_products = cart.get_prods
	quantities = cart.get_quants
	totals = cart.cart_total()
	return render(request, "cart_summary.html", {"cart_products":cart_products,"quantities":quantities,"totals":totals})

def prod_int(prod_size):
   


    # Regular expression pattern to match integer value
    pattern = r'\d+'

    # Find all matches of the pattern in the input string
    matches = re.findall(pattern, prod_size)

    # If there are matches, convert the first match to an integer
    if matches:
        integer_value = int(matches[0])
        print("Integer value:", integer_value)
        return integer_value
 

    
      
def cart_add(request):
    # Get the cart
	cart = Cart(request)
	# test for POST
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))
		product_qty = int(request.POST.get('product_qty'))
		product_size = str(request.POST.get('product_size'))
		product_size1 = prod_int(product_size)
       
		# lookup product in DB
		product = get_object_or_404(Pizza_Menu, Pizza_menu_id=product_id)
		
		# Save to session
		cart.add(product=product, quantity=product_qty,product_price=product_size1)

		# Get Cart Quantity
		cart_quantity = cart.__len__()

		# Return resonse
		# response = JsonResponse({'Product Name: ': product.Pizza_Name})
		response = JsonResponse({'qty': cart_quantity})
		messages.success(request, ("Product Added To Cart..."))
		return response
     

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
		# Get stuff
        product_id = int(request.POST.get('product_id'))
		# Call delete Function in Cart
        cart.delete(product=product_id)
        response = JsonResponse({'product':product_id})
		#return redirect('cart_summary')
        messages.success(request, ("Item Deleted From Shopping Cart..."))
        return response
    

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
		# Get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product_price = str(request.POST.get('product_price'))
        product_price1 = prod_int(product_price)
        cart.update(product=product_id, quantity=product_qty,price=product_price1)
        response = JsonResponse({'qty':product_qty,'price':product_price})
		#return redirect('cart_summary')
        messages.success(request, ("Your Cart Has Been Updated..."))
        return response

		