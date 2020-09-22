from django.db import models
from .models import *
# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length=80)
	reg_number = models.IntegerField(unique=True)
	price = models.DecimalField(decimal_places=2, max_digits=7)
	emi_status = models.BooleanField(default=True)

	def __str__(self):
		return self.name

class Sattlement(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	paid_amount = models.DecimalField(decimal_places=2, max_digits=7)
	date = models.DateField()

	def details(self):
		return f'{self.product.name} - INR {self.product.price}'

	def __str__(self):
		return self.product.name

