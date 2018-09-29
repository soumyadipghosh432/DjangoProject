from django.shortcuts import render, redirect
from .models import Account
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
import sys

# Create your views here.
def register(request):
	return render(request, 'account_/registration.html')

def doRegister(request):
	username = request.POST["username"]
	password = make_password(request.POST["passwd"],salt=None, hasher='default')
	firstName = request.POST["firstName"]
	lastName = request.POST["lastName"]
	email = request.POST["email"]
	
	record = Account()
	record.userName = username
	record.password = password
	record.firstName = firstName
	record.lastName = lastName
	record.email = email
	record.save()
	return redirect('/account/login')
	
	
def login(request):
	return render(request, 'account_/login.html')

def doLogin(request):
	username = request.POST["username"]
	password = request.POST["passwd"]
	
	try:
		record = Account.objects.get(userName = username)
		if record is not None:
			validated = check_password(password, record.password, setter=None, preferred='default')
			if validated:
				return redirect('/account/homepage')
			else:
				return HttpResponse("<h2>Invalid Password</h2>")
	except Account.DoesNotExist:
		return HttpResponse("User not found")
	except Exception as e:
		extype, value, traceback = sys.exc_info()
		return HttpResponse("Exception : "+str(value))
			
def homepage(request):
	return render(request, 'account_/homepage.html')	
			
			
			