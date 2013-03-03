# coding: utf-8

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import User

ASSUNTO = u'assunto'
MENSAGEM = u'mensagem'


class Usuario(models.Model):
	user = models.OneToOneField(User)
	celular = models.ForeignKey('Celular')
	link_facebook = models.TextField()
	ciente = models.BooleanField()

	def get_full_name(self):
		return self.user.get_full_name()

	def __unicode__(self):
		return self.get_full_name()

	#def save(self, *args, **kwargs):
		#send_mail(ASSUNTO, MENSAGEM, 'ola.sociacao@gmail.com',
				#['ola.sociacao@gmail.com'])
		#super(Usuario, self).save(*args, **kwargs)


class Celular(models.Model):
	numero = models.CharField(max_length=15)
	operadora = models.ForeignKey('Operadora')

	def __unicode__(self):
		return '%s - %s'%(self.numero, self.operadora.nome)

class Operadora(models.Model):
    nome = models.CharField(max_length=10)


class Camisa(models.Model):
	descricao = models.CharField(max_length=20)
	foto = models.CharField(max_length=50, blank=True)

	def __unicode__(self):
		return self.descricao


class Item(models.Model):
	camisa = models.ForeignKey(Camisa)
	quantidade = models.IntegerField()

	def __unicode__(self):
		return self.camisa.descricao + ' - ' + str(self.quantidade)

class FormaPagamento(models.Model):
	descricao = models.CharField(max_length=200)

	def __unicode__(self):
		return self.descricao

class Compra(models.Model):
	usuario = models.ForeignKey(Usuario)
	itens = models.ManyToManyField(Item)
	data = models.DateTimeField(auto_now_add=True)
	formaPagamento = models.ForeignKey(FormaPagamento)
	pago = models.BooleanField(default=False)
	entregue = models.BooleanField(default=False)
	#comprovante = models.FileField(upload_to='comprovantes') #file

	def __unicode__(self):
		if self.pago:
			pago = 'Pago: OK'
		else:
			pago = 'Pago: Falta'
		itens = self.itens.all()

		camisas = []
		for item in itens:
			camisas.append('%s - %d'%(item.camisa.descricao, item.quantidade))

		casmisas = ' '.join(camisas)
		return '%s - %s - %s -%s'%(self.data.strftime('%d/%m/%Y - %H:%M'), self.usuario.user.first_name, camisas, pago)

	def file_name(instance, filename):
		return '/comprovantes/%s'
