# coding: utf-8

from django.shortcuts import render
from django.contrib.auth.models import User
from models import Camisa, Usuario, Operadora, Celular, FormaPagamento, Compra, Item
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def handle_uploaded_file(f, nome):
	try:
		nome += '.'+str(f._name).split('.')[-1]
	except:
		pass
	default_storage.save(nome, ContentFile(f.read()))

# Create your views here.
def compra(request):
	context = {}
	
	camisas = Camisa.objects.all()
	operadoras = Operadora.objects.all()
	contas = FormaPagamento.objects.all()
	
	context['camisas'] = camisas
	context['operadoras'] = operadoras
	context['contas'] = contas

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

		handle_uploaded_file(request.FILES['comprovante'], '%s_%s'%(user.email, userp.id))

	return render(request, 'form_compra.html', context)
