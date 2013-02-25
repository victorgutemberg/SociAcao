from django.shortcuts import render
from models import *

# Create your views here.
def compra(request):	
	camisas = Camisa.objects.all()
	return render(request, 'form_compra.html', locals())
