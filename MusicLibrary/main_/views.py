from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'main_/index.html')

def contact(request):
	return render(request, 'main_/contact.html')	