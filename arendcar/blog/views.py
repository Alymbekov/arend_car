from django.shortcuts import render

from .models import Transport

def index(request):
	return render(request , 'auto/index.html',{})

def car(request):

	one_car = Transport.objects.get(pk=1)
	return render(request , 'auto/car.html',{})

def contacts(request):
	return render(request, 'auto/contacts.html',{})

# Create your views here.
