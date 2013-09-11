# coding: utf-8
from django.shortcuts import render
from models import OrdemServico

def home(request):
    #from django.http import HttpResponse
    context = {'lista': OrdemServico.objects.all(),}
    return render(request, 'index.html', context)