# coding: utf-8
from django.forms import ModelForm
from models import *

class OrdemServicoForm(ModelForm):
	class Meta:
		model = OrdemServico

class OrdemServicoItemForm(ModelForm):
    class Meta:
        model = OrdemServicoItem

class ClienteForm(ModelForm):
	class Meta:
		model = Cliente
		exclude = ('tipo',)

class EquipeForm(ModelForm):
    class Meta:
        model = Equipe

class MembroForm(ModelForm):
    class Meta:
        model = Membro    
        exclude = ('tipo',)
