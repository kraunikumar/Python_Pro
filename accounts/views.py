from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
	li= [1,2,3,4,5,6]
	name='krauni'
	arg={'myName':name, 'number':li}
	return render(request, 'accounts/home.html')
