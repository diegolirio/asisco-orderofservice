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
    print "orderservice: %s" % orderservice
    
    items = OrdemServico_OrdemServicoItem.objects.all()
    print "items.count(): %s" % items.count()

    context = {'orderservice': orderservice,
               'items': items,}
    return render(request, 'planilha.html', context)

def orderservice_edit(request, pk):
    print "orderservice_edit(request, pk)..."
    orderservice = get_object_or_404(OrdemServico, pk=pk)
    ositems = orderservice.osositem_os.all()
    form = OrdemServicoForm(instance=orderservice)
    context = {'form': form,
               'os_pk': pk,
               'orderservice': orderservice,
               'ositems': ositems}
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
    orderservice = get_object_or_404(OrdemServico, pk=pk)
    if request.GET.get('confirm') == 'ok':
        orderservice.delete()
        return HttpResponseRedirect(reverse('orderservice_list'))
    else:
        context = {'model_name': 'Ordem de Serviço',
                   'model': orderservice,
                   'url_confirm': reverse('orderservice_delete', args=[orderservice.pk]),
                   'url_cancel': reverse('orderservice_list'),
        }
        return render(request, 'base_delete.html', context)
    

#=== Ordem de Servicos =========================================================================



def ositem(request, os_pk, pk=0):
    if request.method == 'POST':
        return ositem_save(request, os_pk, pk)
    else:
        if int(pk) == 0:
            return ositem_add(request, os_pk)
        else:
            return ositem_edit(request, os_pk, pk)


def ositem_add(request, os_pk):
    form = OrdemServicoItemForm()
    context = {'form': form,
               'os_pk': os_pk,
               'pk': 0}
    return render(request, 'ositem.html', context)


def ositem_edit(request, os_pk, pk):
    print "ositem_edit[ %s ]..." % pk
    ositem = get_object_or_404(OrdemServico_OrdemServicoItem, pk=pk)
    form = OrdemServicoItemForm(instance=ositem)
    context = {'form': form,
               'pk': pk,
               'os_pk': os_pk}
    return render(request, 'ositem.html', context)


def ositem_save(request, os_pk, pk=0):
    form = OrdemServicoItemForm(request.POST)
    if not form.is_valid():
        print "if not form.is_valid():"
        return render(request, 'ositem.html', {'form': form, 'os_pk': os_pk,})

    ositem = form.save(commit=False)
    if int(pk) > 0:
        ositem.id = pk

    #model = form.save(commit=False)
    #dtRec = datetime.datetime.utcnow().replace(tzinfo=utc)
    #model.dataRecebimento = dtRec
    ositem.ordemServico_id = os_pk
    ositem.save()
    return HttpResponseRedirect(reverse('orderservice_edit', args=(os_pk,)))


def ositem_delete(request, pk):
    ositem = get_object_or_404(OrdemServico_OrdemServicoItem, pk=pk)
    if request.GET.get('confirm') == 'ok':
        ositem.delete()
        return HttpResponseRedirect(reverse('orderservice_list'))
    else:
        context = {'model_name': 'Serviço',
                   'model': ositem,
                   'url_confirm': reverse('ositem_delete', args=[ositem.pk]),
                   'url_cancel': reverse('orderservice_list'),
        }
        return render(request, 'base_delete.html', context)


#=== Servicos ==================================================================================
def services(request):
    services = OrdemServicoItem.objects.all()
    context = {'services': services, }
    return render(request, 'service.html', context)


def service(request, pk=0):
    if request.method == 'POST':
        return service_save(request, pk)
    else:
        if int(pk) == 0:
            return service_add(request)
        else:
            return service_edit(request, pk)


def service_add(request):
    print "service_add..."
    form = ServiceForm()
    who_called = request.GET.get('who_called')
    context = {'form': form, 'who_called': who_called, }
    return render(request, 'service.html', context)


def service_edit(request, pk):
    service = get_object_or_404(OrdemServicoItem, pk=pk)
    form = ServiceForm(instance=service)
    context = {'form': form,
               'pk': pk}
    return render(request, 'service.html', context)


def service_save(request, pk=0):
    form = ServiceForm(request.POST)
    who_called = request.POST.get('who_called')
    if not form.is_valid():
        return render(request, 'service.html', {'form': form, 'who_called': 'show'})

    service = form.save(commit=False)
    if int(pk) > 0:
        service.id = pk

    #model = form.save(commit=False)
    #dtRec = datetime.datetime.utcnow().replace(tzinfo=utc)
    #model.dataRecebimento = dtRec
    #service.ordemServico_id = os_pk

    service.save()


    # tratamento p/ quando for chamado por popup =======================#    
    if who_called:
        return render(request, 'service.html', 
            {'services': OrdemServicoItem.objects.all(), 'who_called': 'close'})
    #===================================================================#

    
    return HttpResponseRedirect(reverse('service_list'))


def service_delete(request, pk):
    print "service_delete..."
    service = get_object_or_404(OrdemServicoItem, pk=pk)
    print "service pk: %s" % service.id
    print "request.GET.get('confirm') = %s" % request.GET.get('confirm')
    if request.GET.get('confirm') == 'ok':
        print "confirm = ok"
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
    who_called = request.GET.get('who_called')
    context = {'form': form, 'who_called': who_called, }
    return render(request, 'cliente.html', context)


def cliente_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(instance=cliente)
    context = {'form': form}
    return render(request, 'cliente.html', context)


def cliente_save(request, pk):
    form = ClienteForm(request.POST)
    who_called = request.POST.get('who_called')
    if not form.is_valid():
        return render(request, 'cliente.html', {'form': form, 'who_called': 'show'})

    if int(pk) > 0:
        cliente = form.save(commit=False)
        cliente.id = pk

    form.save()

    # tratamento p/ quando for chamado por popup =======================#    
    if who_called:
        return render(request, 'cliente.html', 
            {'clientes': Cliente.objects.all(), 'who_called': 'close'})
    #===================================================================#

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
    who_called = request.GET.get('who_called')
    context = {'equipes': equipes, 'form': form, 'who_called': who_called,}
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
    who_called = request.POST.get('who_called')
    if not form.is_valid():
        return render(request, 'equipe.html', {'form': form, 'who_called': who_called,})

    if int(pk) > 0:
        equipe = form.save(commit=False)
        equipe.id = pk

    form.save()

    # tratamento p/ quando for chamado por popup =======================    
    if who_called:
        return render(request, 'equipe.html', 
            {'membros': Equipe.objects.all(), 'who_called': 'close'})
    #===================================================================


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
    who_called = request.POST.get('who_called')

    if not form.is_valid():
        return render(request, 'membro.html', {'form': form, 'who_called': 'show'})

    if int(pk) > 0:
        membro = form.save(commit=False)
        membro.id = pk

    form.save()

    # tratamento p/ quando for chamado por popup =======================    
    if who_called:
        return render(request, 'membro.html', 
            {'membros': Membro.objects.all(), 'who_called': 'close'})
    #===================================================================

	return HttpResponseRedirect(reverse('membro_list'))

def membro_edit(request, pk):
	membro = get_object_or_404(Membro, pk=pk)
	form = MembroForm(instance=membro)
	context = {'form': form,}
	return render(request, 'membro.html', context)

def membro_add(request):
    form = MembroForm()
    who_called = request.GET.get('who_called')
    context = {'membros': membros, 'form': form, 'who_called': who_called,}
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
