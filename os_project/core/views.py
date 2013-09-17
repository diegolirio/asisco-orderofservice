# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
#from models import OrdemServico

@login_required(login_url='/login/')
def home(request):
    context = None #{'lista': OrdemServico.objects.all(),}
    return render(request, 'index.html', context)

def orderservice(request, pk):
    context = {}
    return render(request, 'orderservice.html', context)