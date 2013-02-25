from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Usuario(models.Model):
	nome = models.CharField(max_length=30)
	sobrenome = models.CharField(max_length=30)
	celular = models.CharField(max_length=15)
	link_facebook = models.TextField()

	def get_full_name(self):
		return '%s %s'%(self.nome, self.sobrenome)

	def __unicode__(self):
		return self.get_full_name()

class Camisa(models.Model):
	descricao = models.CharField(max_length=20)
	foto = models.CharField(max_length=50, blank=True)

	def __unicode__(self):
		return self.descricao

class Item(models.Model):
	camisa = models.ForeignKey(Camisa)
	quantidade = models.IntegerField()

class Compra(models.Model):
	usuario = models.ForeignKey(Usuario)
	itens = models.ManyToManyField(Item)
	data = models.DateTimeField(auto_now_add=True)

	def quantidade_itens(self):
		return self.itens.count()

	def __unicode__(self):
		return '%s - %s'%(str(self.data), self.usuario.get_full_name())

