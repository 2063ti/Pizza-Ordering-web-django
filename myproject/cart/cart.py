from pizza.models import *

class Cart():
	def __init__(self, request):
		self.session = request.session
		# Get request
		self.request = request
		# Get the current session key if it exists
		cart = self.session.get('session_key')

		# If the user is new, no session key!  Create one!
		if 'session_key' not in request.session:
			cart = self.session['session_key'] = {}


		# Make sure cart is available on all pages of site
		self.cart = cart
		
	def add(self,product, quantity,product_price):
	
		product_id = str(product.Pizza_menu_id)
		product_qty = str(quantity)
		product_price = str(product_price)
		# Logic
		if product_id in self.cart:
			pass
		else:
			#self.cart[product_id] = {'price': str(product.price)}
			self.cart[product_id] = {'price': str(product_price),'Quantity':str(product_qty)}
			# self.cart[product_id] = int(product_qty)
			# self.cart[product_id] = int(product_price)

		self.session.modified = True
		# Deal with logged in user
		if self.request.user.is_authenticated:
			# Get the current user profile
			current_user = CustomUser.objects.filter(id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
			current_user.update(old_cart=str(carty))
		
	def __len__(self):
		return len(self.cart)
	
	def get_prods(self):
		# Get ids from cart
		product_ids = self.cart.keys()
		# Use ids to lookup products in database model
		products = Pizza_Menu.objects.filter(Pizza_menu_id__in=product_ids)

		# Return those looked up products
		return products
	
	def  get_quants(self):
		quantities = self.cart
		return quantities
	
	def update(self, product, quantity,price):
		product_id = str(product)
		product_qty = int(quantity)
		product_price = int(price)

		# Get cart
		ourcart = self.cart
		# Update Dictionary/cart
		ourcart[product_id]["Quantity"] = product_qty
		ourcart[product_id]["price"] = product_price

		self.session.modified = True
	

		# Deal with logged in user
		if self.request.user.is_authenticated:
			# Get the current user profile
			current_user = CustomUser.objects.filter(id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
			current_user.update(old_cart=str(carty))


		thing = self.cart
		return thing	
		
		
   
	
	def delete(self, product):
		product_id = str(product)
		# Delete from dictionary/cart
		if product_id in self.cart:
			del self.cart[product_id]

		self.session.modified = True

		# Deal with logged in user
		if self.request.user.is_authenticated:
			# Get the current user profile
			current_user = CustomUser.objects.filter(id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
			current_user.update(old_cart=str(carty))
		
	def cart_total(self):
		# Get product IDS
		product_ids = self.cart.keys()
		# lookup those keys in our products database model
		products = Pizza_Menu.objects.filter(Pizza_menu_id__in=product_ids)
		# Get quantities
		quantities = self.cart
		# Start counting at 0
		total = 0
		
		for key, value in quantities.items():
			# Convert key string into int so we can do math
			key = int(key)
			for product in products:
				if product.Pizza_menu_id == key:
					if product.is_sale:
						total = total + ((int(value["price"])-(int(value["price"] )* product.sale_price)/100))*int(value['Quantity'])
					else:
						total = total + (int(value["price"]) * int(value["Quantity"]))



		return total
	
	def db_add(self, product,price, quantity):
		product_id = str(product)
		product_qty = str(quantity)
		product_price = str(price)
		# Logic
		if product_id in self.cart:
			pass
		else:
			#self.cart[product_id] = {'price': str(product.price)}
			self.cart[product_id] = {'price': int(product_price),'Quantity':int(product_qty)}

		self.session.modified = True

		# Deal with logged in user
		if self.request.user.is_authenticated:
			# Get the current user profile
			current_user = CustomUser.objects.filter(id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
			current_user.update(old_cart=str(carty))



	

			