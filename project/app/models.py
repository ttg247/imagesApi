from django.db import models

# Create your models here.
class Picture(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    src = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    categories = models.CharField(max_length=100,blank=False, default='')
    price = models.CharField(max_length=10,blank=False, default='')
    published = models.BooleanField(default=False)

class Order(models.Model):
    user = models.CharField(max_length=10, blank=False, default='')
    picture = models.CharField(max_length=70, blank=False, default='')
    quantity = models.CharField(max_length=70, blank=False, default='')
    status = models.BooleanField(default=False)
    date = models.CharField(max_length=200,blank=False, default='')
    time = models.CharField(max_length=10,blank=False, default='')

class User(models.Model):
    fname = models.CharField(max_length=10, blank=False, default='')
    lname = models.CharField(max_length=70, blank=False, default='')
    email = models.CharField(max_length=70, blank=False, default='')
    address = models.CharField(max_length=30,blank=False, default='')
    phone = models.CharField(max_length=10,blank=False, default='')