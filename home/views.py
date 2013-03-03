# coding: utf-8

from django.shortcuts import render
from django.contrib.auth.models import User
from models import Camisa, Usuario, Operadora, Celular, FormaPagamento, Compra, Item
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os

def handle_uploaded_file(f, nome, path=''):
	try:
		nome += '.'+str(f._name).split('.')[-1]
	except:
		pass

	if path:
		path = os.path.join(path, nome)
	else:
		path = nome
		
	default_storage.save(path, ContentFile(f.read()))

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
		erro = False
		operadora = request.POST.get('operadora')
		email = request.POST.get('email')
		nome = request.POST.get('nome')
		ciente = request.POST.get('ciente')
		celular = request.POST.get('celular')
		facebook = request.POST.get('facebook')
		conta = request.POST.get('conta')

		context['operadora'] = operadora
		context['email'] = email
		context['nome'] = nome
		context['ciente'] = ciente
		context['celular'] = celular
		context['facebook'] = facebook
		context['conta_id'] = int(conta)


		if 'comprovante' not in request.FILES:
			context['msg'] = 'Por favor, anexe o seu comprovante!'
			erro = True

		if not operadora:
			erro = True
			context['msg'] = 'Por favor, escolha uma operadora!'

		if not email:
			erro = True
			context['msg'] = 'O email é obrigatório!'

		if not nome:
			erro = True
			context['msg'] = 'O nome é obrigatório!'

		if not conta:
			erro = True
			context['msg'] = 'Escolha a conta em que fez o depósito!'


		if not erro:
			try:
				userExists = False
				user = User()
				user.first_name = nome
				user.email = email
				user.username = email[:30]
				user.save()
			except:
				userExists = True
				user = User.objects.get(username=email[:30])

			if userExists:
				try:
					userp = Usuario.objects.get(user=user)
				except:
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
			compra.formaPagamento_id = conta
			compra.save()

			for camisa in [x for x in request.POST if x.startswith('camisa_')]:
				if request.POST[camisa] != '0':
					item = Item()
					item.camisa_id = camisa[7:]
					item.quantidade = request.POST[camisa]
					item.save()
					compra.itens.add(item)

			handle_uploaded_file(request.FILES['comprovante'], '%s_%s'%(user.email, userp.id), 'comprovantes')

	return render(request, 'form_compra.html', context)
