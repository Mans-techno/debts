from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Shop(models.Model):
    title = models.CharField(max_length=50)
    owner_name = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    

class Debts(models.Model):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='shop')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    phone = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name 

