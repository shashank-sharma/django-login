from django.shortcuts import render
from django.http import Http404, HttpResponse
from login.models import PhoneDetails

def home(request):
	try:
		p = PhoneDetails
		p = p.objects.filter(username=request.user)
	except:
		print('Nothing')
	return render(request, 'home.html', {'data': p[0]})

def about(request):
    return render(request, 'about.html', {})

def success(request):
    return render(request, 'success.html', {})
