from django.contrib import admin
from .models import  Collection,Promotion,Product,Customer, Order,Address,Cart, CartItem, OrderItem

admin.site.register(Collection)
admin.site.register(Promotion)  
admin.site.register(Product)  
admin.site.register(Customer)  
admin.site.register(Order)  
admin.site.register(Address)  
admin.site.register(Cart)  
admin.site.register(CartItem)  
admin.site.register(OrderItem)  

  