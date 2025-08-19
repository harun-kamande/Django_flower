from django.db import models

# Create your models here.


class Users(models.Model):
    date_joined = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    user_type = models.CharField(max_length=50 , default='customer')

    def __str__(self):
        return self.username
    

class Flower(models.Model):
    name=models.CharField(max_length=1000,null=False)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField(null=True, blank=True)
    image=models.ImageField(upload_to='flowers/', null=True, blank=True)
    remainig=models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    date_ordered = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)
    delivery_address=models.CharField(max_length=255)

    def __str__(self):
        return super().__str__()
    

class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    flower=models.ForeignKey(Flower, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Order {self.id} for {self.quantity} of {self.flower.name}"
