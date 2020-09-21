from django.shortcuts import render
from .models import *
from django.db.models import Sum, Count


def dashboard(request):
	productData = Product.objects.all() # Fetching Products Data (PK)
	context={
		'productData':productData,
	}
	return render(request, 'app/dashboard.html', context)


def get_emi_details(request, pk):
	productData = Product.objects.get(id=pk) # Fetching Product Data (PK)
	settlementData = Sattlement.objects.filter(product__id=pk) # Fetching Settlement Data (PK)

	total = settlementData.aggregate(Sum('paid_amount')) # Total Amount Paid on EMI
	total_emi = settlementData.aggregate(Count('paid_amount')) # Total Attempt of EMIs
	due_amount = (productData.price - total['paid_amount__sum']) # Due Amount of EMI
	if due_amount == 0:
		Product.objects.filter(id=pk).update(emi_status=False) # If EMI is Completed EMI Status Set to False
	context={
		'productData': productData,
		'settlementData' : settlementData,
		'due_amount' : due_amount,
		'total_emi' : total_emi,
	}
	return render(request, 'app/emi_status.html', context)
