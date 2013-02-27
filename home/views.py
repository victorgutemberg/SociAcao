# coding: utf-8

from django.shortcuts import render
from models import Camisa, Usuario, Operadora, Celular


def compra(request):
    # TODO: Refatorar código com forms
    context = {}
    camisas = Camisa.objects.all()
    context['camisas'] = camisas
    if request.method == 'POST':
        usuario = Usuario()
        usuario.nome = request.POST['nome']
        usuario.email = request.POST['email']
        operadora = Operadora()
        operadora.nome = request.POST['operadora']
        operadora.save()
        celular = Celular()
        celular.numero = request.POST['celular']
        celular.operadora = operadora
        celular.save()
        usuario.celular = celular
        usuario.link_facebook = request.POST['facebook']
        usuario.save()
    return render(request, 'form_compra.html', locals())
