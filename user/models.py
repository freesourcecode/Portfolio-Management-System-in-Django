from django.db import models

# Create your models here.


class Stocks(models.Model):

    name = models.CharField(max_length=200, help_text="Enter Stock Name")
    description = models.TextField(help_text="Enter Product Description")
    unitCost = models.FloatField(default=0.0,help_text="Enter Stock Unit Cost")
    unit = models.CharField(max_length=10,help_text="Enter Stock Unit ")
    quantity = models.IntegerField(default=0,help_text="Enter Stock Quantity")
    open = models.FloatField(default=0.0)
    high = models.FloatField(default=0.0)
    low = models.FloatField(default=0.0)
    close = models.FloatField(default=0.0)
    volume = models.IntegerField(default=0)
    symb = models.CharField(max_length=5,help_text="Enter Symbol")
    #user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name


class User(models.Model):

    name = models.CharField(max_length=200, help_text="Enter User Name")
    username = models.CharField(max_length=200, help_text="Enter User Name",default="null")
    mobile = models.IntegerField(null=True)
    email = models.CharField(max_length=200,null=True)
    password = models.CharField(max_length=10)
    description = models.TextField(help_text="Enter User Description")
    stock_no = models.IntegerField(default=0)
    portfolio_val = models.IntegerField(default=0.0)
    stock = models.ForeignKey(Stocks, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.name

class Transaction(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    stock = models.ForeignKey(Stocks, on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(default=0,help_text="Enter Stock Quantity")
    Val = models.FloatField(default=0.0)


