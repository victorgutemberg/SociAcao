# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Usuario(models.Model):
	user = models.OneToOneField(User)
	celular = models.ForeignKey('Celular')
	link_facebook = models.TextField()
	ciente = models.BooleanField()

	def __unicode__(self):
		return self.user.get_full_name()

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

	def file_name(instance, filename):
		return '/comprovantes/%s'

	def quantidade_itens(self):
		return self.itens.count()

	def __unicode__(self):
		if self.pago:
			pago = 'Pago: OK'
		else:
			pago = 'Pago: Falta'
		return '%s - %s - %s'%(self.data.strftime('%d/%m/%Y - %H:%M'), self.usuario.user.first_name, pago)

