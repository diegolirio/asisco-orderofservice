# coding: utf-8
from django.forms import ModelForm
from models import *

class OrdemServicoForm(ModelForm):
	class Meta:
		model = OrdemServico


class ClienteForm(ModelForm):
	class Meta:
		model = Cliente
		exclude = ('tipo',)