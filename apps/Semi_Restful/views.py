from django.shortcuts import render, HttpResponse, redirect
from models import Product
# from django.core.urlresolvers import reverse
# from django.db.models import Count 

def index(request):
   displayAll = Product.objects.all()
   context = {
   		'displayAll': displayAll
   }
   print "yo"
   return render(request, 'Semi_Restful/index.html', context)

def show(request, id):
	showproduct = Product.objects.filter(id = id)
	context = {
		'showproducts': showproduct
	}
	return render(request, 'Semi_Restful/show1.html', context)

def editDisplay(request, id):
	editproduct = Product.objects.filter(id = id)
	context = {
		'editproducts': editproduct
	}
	return render(request, 'Semi_Restful/edit.html', context)

def edit(request, id):
	Product.objects.filter(id = id).update(name = request.POST['name'], description = request.POST['description'], price = request.POST['price'])
	return redirect ('index')

def createDisplay(request):
	return render(request, 'Semi_Restful/addnew.html')

def create(request):
	print "hello"
	Product.objects.create(name = request.POST['name'], description = request.POST['description'], price = request.POST['price'])
	return redirect ('index')

def delete(request, id):
	Product.objects.filter(id = id).delete()
	return redirect ('index')


