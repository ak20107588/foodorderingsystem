from django.db import models

# Create your models here.



class Product(models.Model):
    ProductID=models.AutoField(primary_key=True)
    ProductName=models.CharField(max_length=255)
    ProductImage= models.CharField(max_length=255)
    ProductPrice= models.BigIntegerField()
    ProductOffer=models.BooleanField()
    OfferPrice=models.BigIntegerField()

class Order(models.Model):
    OrderID=models.AutoField(primary_key=True)
    UserID=models.ForeignKey("app1.User",on_delete=models.CASCADE)
    TotalPrice=models.BigIntegerField()
    TotalQuantity=models.BigIntegerField()
    OrderDate=models.DateTimeField((""), auto_now=True)

class User(models.Model):
    UserID=models.AutoField(primary_key=True)
    UserName=models.CharField(max_length=255)
    UserEmail=models.EmailField(max_length=255)
    UserMobile=models.BigIntegerField()
    Address=models.CharField(max_length=255)
    PaymentMethod=models.CharField(max_length=255)

class Cart(models.Model):
    ProductID=models.ForeignKey("app1.Product",on_delete=models.CASCADE)
    TotalQantity=models.BigIntegerField(default=0)
    TotalPrice=models.BigIntegerField()


class Customers(models.Model):
    Name = models.CharField(max_length=250)
    Email = models.EmailField(max_length=254)
    Mobile = models.BigIntegerField()
    Password = models.CharField( max_length=250)





