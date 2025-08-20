from django.contrib import admin
from .models import Users, Flower, Order, OrderItem
# Register your models here.
admin.site.register(Users)
admin.site.register(Flower)
admin.site.register(Order)
admin.site.register(OrderItem)