from django.shortcuts import render
from django.contrib.auth.models import User
from models import *

# Create your views here.
def compra(request):
	if request.method == 'POST':
		nome = request.POST.get('nome')
		email = request.POST.get('email')
		
		ciente = request.POST.get('ciente')
		celular = request.POST.get('celular')
		operadora = request.POST.get('operadora')
		facebook = request.POST.get('facebook')

		user = User()
		user.first_name = nome
		user.email = email
		user.username = email[:30]
		user.save()

		userp = Usuario()
		userp.user = user
		userp.ciente = ciente
		userp.facebook = facebook

		celular = Celular(numero=celular, operadora_id=operadora)
		celular.save()

		userp.celular = celular
		userp.save()

		compra = Compra()
		compra.usuario = userp
		compra.formaPagamento_id = request.POST.get('conta')
		compra.save()

		for camisa in [x for x in request.POST if x.startswith('camisa_')]:
			if request.POST[camisa] != '0':
				item = Item()
				item.camisa_id = camisa[7:]
				item.quantidade = request.POST[camisa]
				item.save()
				compra.itens.add(item)


	camisas = Camisa.objects.all()
	operadoras = Operadora.objects.all()
	contas = FormaPagamento.objects.all()

	return render(request, 'form_compra.html', locals())