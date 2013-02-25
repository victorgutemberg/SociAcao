from django.shortcuts import render
from models import *

# Create your views here.
def compra(request):
	if request.method == 'POST':
		usuario = Usuario()
		usuario.nome = request.POST.get('nome')
		usuario.sobrenome = request.POST.get('sobrenome')
		usuario.celular = request.POST.get('celular')
		usuario.link_facebook = request.POST.get('facebook')
		usuario.save()

	
	camisas = Camisa.objects.all()

	return render(request, 'form_compra.html', locals())
