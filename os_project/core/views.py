# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from models import *
from forms import *

@login_required(login_url='/login/')
def home(request):
    context = {'lista': OrdemServico.objects.all(),}
    return render(request, 'index.html', context)

#=== Ordem de Servicos =========================================================================
def orderservice(request, pk=None):
	if request.method == 'POST':
		return orderservice_save(request, pk)
	else:
		if int(pk) == 0:
			return orderservice_add(request)
		else:
			return orderservice_edit(request, pk) 


def orderservice_list(request):
    context = {}
    return render(request, 'orderservices.html', context)


def orderservice_add(request):
	form = OrdemServicoForm()
	context = {'form': form,}
	return render(request, 'orderservice_form.html', context)

def orderservice_edit(request, pk):
	from django.http import HttpResponse
	return HttpResponse('\o/ os edit')


def orderservice_save(request, pk):
	form = OrdemServicoForm(request.POST)
	if not form.is_valid():
		return render(request, 'orderservice_form.html', {'form': form,})


def orderservice_delete(request, pk):
	pass

#=== Ordem de Servicos =========================================================================


#=== Cliente ===================================================================================
def clientes(request):
	clientes = Cliente.objects.all()
	context = {'clientes': clientes,}
	return render(request, 'cliente.html', context)

def cliente(request, pk=0):
	if request.method == 'POST':
		return cliente_save(request, pk)
	else:
		if int(pk) == 0:
			return cliente_add(request)
		else:
			return cliente_edit(request, pk)

def cliente_add(request):
	form = ClienteForm()
	context = {'form': form,}
	return render(request, 'cliente.html', context) 

def cliente_edit(request, pk):
	cliente = get_object_or_404(Cliente, pk=pk)
	form  = ClienteForm(instance=cliente)
	context = {'form': form}
	return render(request, 'cliente.html', context)

def cliente_save(request, pk):
	form = ClienteForm(request.POST)
	if not form.is_valid():
		return render(request, 'cliente.html', {'form': form,})

	if int(pk) > 0:
		cliente = form.save(commit=False)
		cliente.id = pk

	form.save()
	return HttpResponseRedirect(reverse('cliente_list'))

def cliente_delete(request, pk):
	cliente = get_object_or_404(Cliente, pk=pk)
	if request.GET.get('confirm') == 'ok':
		cliente.delete()
		return HttpResponseRedirect(reverse('cliente_list'))
	else:
		context = {'model_name': 'Cliente',
				   'model': cliente,
				   'url_confirm': reverse('cliente_delete', args=[cliente.pk]),
				   'url_cancel': reverse('cliente_list'),
				   }
		return render(request, 'base_delete.html', context)

#=== Cliente ===================================================================================	

