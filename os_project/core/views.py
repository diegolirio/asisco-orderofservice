# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from models import *
from forms import *

@login_required(login_url='/login/')
def home(request):
    context = {'lista': OrdemServico.objects.all(),}
    return render(request, 'index.html', context)


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
    return render(request, 'orderservice.html', context)


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


def cliente(request, pk):
	if request.method == 'POST':
		pass
	else:
		if int(pk) == 0:
			return cliente_add(request)
		else:
			pass	


def cliente_add(request):
	form = ClienteForm()
	context = {'form': form,}
	return render(request, 'cliente_form.html', context) 

