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

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)