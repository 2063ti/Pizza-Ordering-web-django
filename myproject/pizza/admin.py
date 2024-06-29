from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Pizza_type)
admin.site.register(Pizza_Menu)
admin.site.register(order)
admin.site.register(order_Items)
admin.site.register(ShippingAddress)
admin.site.register(ContactUs)
admin.site.register(Feedback)