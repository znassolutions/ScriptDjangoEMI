from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'reg_number', 'price','emi_status']

@admin.register(Sattlement)
class SattlementAdmin(admin.ModelAdmin):
	list_display = ['details', 'paid_amount', 'date']