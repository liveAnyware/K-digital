from django.db import models

# Create your models here.

class User(models.Model) :
    id = models.TextField(max_length=100, primary_key= True)
    pwd = models.TextField(max_length=100)
    name = models.TextField(max_length=100)
    account = models.CharField(max_length= 100)
    amount = models.IntegerField(default= 30000000)

class Comp(models.Model):
    code = models.CharField(max_length= 100, primary_key= True)
    comp_name = models.CharField(max_length= 100)
    market = models.CharField(max_length= 100)
    stock_amt = models.IntegerField()

class Order(models.Model):
    comp_code = models.ForeignKey('Comp',
                                  related_name= 'comp',
                                  on_delete= models.CASCADE,
                                  db_column='comp_code')
    price = models.IntegerField()
    ord_amt = models.IntegerField()
    buyer = models.ForeignKey('User',
                              on_delete= models.CASCADE,
                              db_column='buyer')
    seller = models.ForeignKey('User',
                              on_delete=models.CASCADE,
                              db_column='seller')

class Balance(models.Model):
    owner = models.ForeignKey('User',
                              on_delete= models.CASCADE,
                              db_column='owner')
    comp_code = models.ForeignKey('Comp',
                                  related_name='comp',
                                  on_delete=models.CASCADE,
                                  db_column='comp_code')
    price = models.IntegerField()
    ord_amt = models.IntegerField()



