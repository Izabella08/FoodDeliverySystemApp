from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Product)
admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(AdministratorRestaurant)
admin.site.register(DeliveryGuy)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(ProductEditDetailsForm)
