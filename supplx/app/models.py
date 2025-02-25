from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    pro_id=models.TextField()
    name=models.TextField()
    price=models.IntegerField()
    offer_price=models.IntegerField()
    img=models.FileField()
    des=models.TextField()
    stock = models.IntegerField(default=0)  # Stock field

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)  # Quantity field

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

class Buy(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.IntegerField()
    data=models.DateField(auto_now_add=True)