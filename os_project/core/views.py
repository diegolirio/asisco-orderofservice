# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from models import *
from forms import *
import datetime


@login_required(login_url='/login/')
def home(request):
    context = {'lista': OrdemServico.objects.all(), }
    return render(request, 'index.html', context)

#=== Ordem de Servicos =========================================================================
def orderservice(request, pk=0):
    if request.method == 'POST':
        return orderservice_save(request, pk)
    else:
        if int(pk) == 0:
            return orderservice_add(request)
        else:
            return orderservice_edit(request, pk)


def orderservices(request):
    context = {'lista': OrdemServico.objects.all(),}
    return render(request, 'orderservices.html', context)


def orderservice_add(request):
    print "orderservice_add(request)..."
    form = OrdemServicoForm()
    services = OrdemServico_OrdemServicoItem.objects.all()
    context = {'form': form}
    return render(request, 'orderservice_form.html', context)

def print_os(request, pk):
    orderservice = get_object_or_404(OrdemServico, pk=pk)
    items = OrdemServico_OrdemServicoItem.objects.all()
    context = {'orderservice': orderservice,
               'items': items,}
    return render(request, 'planilha.html', context)

def orderservice_edit(request, pk):
    print "orderservice_edit(request, pk)..."
    orderservice = get_object_or_404(OrdemServico, pk=pk)
    services = orderservice.osositem_os.all()
    form = OrdemServicoForm(instance=orderservice)
    context = {'form': form,
               'os_pk': pk,
               'orderservice': orderservice,
               'services': services}
    return render(request, 'orderservice_form.html', context)


def orderservice_save(request, pk=0):
    form = OrdemServicoForm(request.POST, request.FILES)
    if not form.is_valid():
        return render(request, 'orderservice_form.html', {'form': form, })

    os = form.save(commit=False)
    if int(pk) > 0:
        os.id = pk

    os.save()
    #return HttpResponseRedirect(reverse('service_add', args=(os.id,)))
    context = {'os': os}
    return render(request, 'os_save_ok.html', context)



def orderservice_delete(request, pk):
    pass

#=== Ordem de Servicos =========================================================================


#=== Servicos ==================================================================================
def services(request):
    services = OrdemServicoItem.objects.all()
    context = {'services': services, }
    return render(request, 'service.html', context)


def service(request, os_pk, pk=0):
    print "service(request, pk, os_pk):..."
    if request.method == 'POST':
        return service_save(request, os_pk, pk)
    else:
        if int(pk) == 0:
            return service_add(request, os_pk)
        else:
            return service_edit(request, os_pk, pk)


def service_add(request, os_pk):
    form = OrdemServicoItemForm()
    context = {'form': form,
               'os_pk': os_pk,
               'pk': 0}
    return render(request, 'service.html', context)


def service_edit(request, os_pk, pk):
    service = get_object_or_404(OrdemServicoItem, pk=pk)
    form = OrdemServicoItemForm(instance=service)
    context = {'form': form,
               'pk': pk,
               'os_pk': os_pk}
    return render(request, 'service.html', context)


def service_save(request, os_pk, pk=0):
    form = OrdemServicoItemForm(request.POST)
    if not form.is_valid():
        return render(request, 'service.html', {'form': form, 'os_pk': os_pk,})

    service = form.save(commit=False)
    if int(pk) > 0:
        service.id = pk

    #model = form.save(commit=False)
    #dtRec = datetime.datetime.utcnow().replace(tzinfo=utc)
    #model.dataRecebimento = dtRec
    service.ordemServico_id = os_pk
    service.save()
    return HttpResponseRedirect(reverse('orderservice', args=(os_pk,)))


def service_delete(request, pk):
    service = get_object_or_404(OrdemServicoItem, pk=pk)
    if request.GET.get('confirm') == 'ok':
        service.delete()
        return HttpResponseRedirect(reverse('service_list'))
    else:
        context = {'model_name': 'Serviço',
                   'model': service,
                   'url_confirm': reverse('service_delete', args=[service.pk]),
                   'url_cancel': reverse('service_list'),
        }
        return render(request, 'base_delete.html', context)
#=== Servicos ==================================================================================

#=== Cliente ===================================================================================
def clientes(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes, }
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
    context = {'form': form, }
    return render(request, 'cliente.html', context)


def cliente_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(instance=cliente)
    context = {'form': form}
    return render(request, 'cliente.html', context)


def cliente_save(request, pk):
    form = ClienteForm(request.POST)
    if not form.is_valid():
        return render(request, 'cliente.html', {'form': form, })

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


#=== Equipe ====================================================================================

def equipes(request):
    equipes = Equipe.objects.all()
    context = {'equipes': equipes, }
    return render(request, 'equipe.html', context)


def equipe(request, pk=0):
    if request.method == 'POST':
        return equipe_save(request, pk)
    else:
        if int(pk) == 0:
            return equipe_add(request)
        else:
            return equipe_edit(request, pk)


def equipe_add(request):
    form = EquipeForm()
    context = {'equipes': equipes,
               'form': form}
    return render(request, 'equipe.html', context)


def equipe_edit(request, pk):
    equipe = get_object_or_404(Equipe, pk=pk)
    form = EquipeForm(instance=equipe)
    membros = form.instance.membro_equipe.all()
    context = {'form': form,
               'membros': membros,
               'equipe_pk': pk,
               'equipe': equipe,}
    return render(request, 'equipe.html', context)


def equipe_save(request, pk):
    form = EquipeForm(request.POST)
    if not form.is_valid():
        return render(request, 'equipe.html', {'form': form, })

    if int(pk) > 0:
        equipe = form.save(commit=False)
        equipe.id = pk

    form.save()
    return HttpResponseRedirect(reverse('equipe_list'))

def equipe_delete(request, pk):
    equipe = get_object_or_404(Equipe, pk=pk)
    if request.GET.get('confirm') == 'ok':
        equipe.delete()
        return HttpResponseRedirect(reverse('equipe_list'))
    else:
        context = {'model_name': 'Equipe',
                   'model': equipe,
                   'url_confirm': reverse('equipe_delete', args=[equipe.pk]),
                   'url_cancel': reverse('equipe_list'),
                   }
    return render(request, 'base_delete.html', context)

#=== Equipe ====================================================================================

#=== Membro ====================================================================================
def membros(request):
    membros = Membro.objects.all()
    context = {'membros': membros, }
    return render(request, 'membro.html', context)

def membro(request, pk=0):
	if request.method == 'POST':
		return membro_save(request, pk)
	else:
		if int(pk) == 0:
			return membro_add(request)
		else:
			return membro_edit(request, pk)

def membro_save(request, pk):
	form = MembroForm(request.POST)
	if not form.is_valid():
		return render(request, 'membro.html', {'form': form})

	if int(pk) > 0:
		membro = form.save(commit=False)
		membro.id = pk

	form.save()
	return HttpResponseRedirect(reverse('membro_list'))

def membro_edit(request, pk):
	membro = get_object_or_404(Membro, pk=pk)
	form = MembroForm(instance=membro)
	context = {'form': form,}
	return render(request, 'membro.html', context)

def membro_add(request):
    form = MembroForm()
    context = {'membros': membros,
			   'form': form,}
    return render(request, 'membro.html', context)

def membro_add_equipe(request):
    form = MembroForm()
    form.instance.equipe = Equipe.objects.get(pk=request.GET.get('equipe'))
    context = {'membros': membros,
			   'form': form,}
    return render(request, 'membro_form_popup.html', context)

def membro_save_equipe(request):
    form = MembroForm(request.POST)
    if not form.is_valid():
        return render(request, 'membro_form_popup.html', {'form': form})

    form.save()
    context = {'membros': membros,
               'form': form,
               'status_transaction': 'S',
               'message': 'Membro de equipe salvo com sucesso!',}
    return render(request, 'membro_form_popup.html', context)

def membro_delete(request, pk):
	membro = get_object_or_404(Membro, pk=pk)
	if request.GET.get('confirm') == 'ok':
		membro.delete()
		return HttpResponseRedirect(reverse('membro_list'))
	else:
		context = {'model_name': 'Membro',
				   'model': membro,
				   'url_confirm': reverse('membro_delete', args=[membro.pk]),
				   'url_cancel': reverse('membro_list'),
				   }
		return render(request, 'base_delete.html', context)

#=== Membro ====================================================================================
