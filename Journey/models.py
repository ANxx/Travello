from django.db import models


# Create your models here.

class Place(models.Model):

    name = models.CharField(max_length=50, default="")
    img = models.ImageField(upload_to='pics', default="")
    price = models.IntegerField(default=0)
    des = models.TextField(default='')
    offer = models.BooleanField(default=False)
