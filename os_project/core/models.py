# coding: utf-8
from django.db import models
from django.utils import timezone

PESSOA_TIPO_CHOICES = (
        ('CLI', u'Cliente'),
        ('MEM', u'Membro de Equipe'),
    )


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)    

    def __unicode__(self):
        return self.nome


class Cliente(Pessoa):
    tipo = models.CharField(max_length=3, choices=PESSOA_TIPO_CHOICES, default='CLI')



class Equipe(models.Model):
    nome = models.CharField('Nome da Equipe', max_length=100)

    def __unicode__(self):
        return self.nome


class Membro(Pessoa):
    tipo = models.CharField(max_length=3, choices=PESSOA_TIPO_CHOICES, default='MEM')
    equipe = models.ForeignKey('Equipe', related_name='membro_equipe')


class OrdemServicoItem(models.Model):
    numero = models.CharField(u'Numero de Desenvo/Conjunto/Peça', max_length=100) 
    denominacao = models.CharField(u'Denominação', max_length=200)

    def __unicode__(self):
        return "%s - %s" % (self.numero, self.denominacao)


class OrdemServico(models.Model):
    numero = models.CharField(u'Ordem de Serviço', max_length=50)
    projetoNome = models.CharField(u'Nome do Projeto', max_length=100)
    cliente = models.ForeignKey('Cliente', verbose_name=u'Cliente', related_name='os_cliente')
    numeroOP = models.CharField(u'Nº.OP', max_length=20)
    equipamento = models.CharField(max_length=100)
    referencia = models.CharField(u'Referencia/Nº de Desenho', max_length=100)
    realizadoPor = models.ForeignKey('Membro', verbose_name=u'Realizado Por', related_name='os_realizadopor')
    realizadoData = models.DateTimeField(u'Data Realizado')
    verificadoPor = models.ForeignKey('Membro', verbose_name=u'Verificado Por', related_name='os_verificadopor')
    verificadoData = models.DateTimeField(u'Data Verificado')
    responsavel = models.ForeignKey('Membro', verbose_name=u'Responsavel Projeto', related_name='os_responsavel')
    revisao = models.CharField(u'Revisão', max_length=20)
    revisaoData = models.DateTimeField(u'Data da Revisão')
    revisadoPor = models.ForeignKey('Membro', verbose_name=u'Revisado Por', related_name='os_revisadopor')
    entregaPrazo = models.CharField(u'Prazo de Entrega', max_length=50)
    entregaLugar = models.CharField(u'Lugar de Entrega', max_length=250, blank=True)
    totalConjunto = models.IntegerField(u'Total de Conjuntos')
    items = models.ManyToManyField(OrdemServicoItem, through='OrdemServico_OrdemServicoItem', null=True, blank=True)
    equipe = models.ForeignKey('Equipe')

    def __unicode__(self):
        return "%s - %s" % (self.projetoNome, self.numero)


class OrdemServico_OrdemServicoItem(models.Model):
    ordemServico = models.ForeignKey('OrdemServico', related_name='osositem_os')
    item = models.ForeignKey('OrdemServicoItem', related_name='osositem_item')
    quantidade = models.IntegerField()
    acabamento = models.CharField(u'Acabamento/RAL', max_length=100)
    observacoes = models.TextField(u'Observações')
    fabricar = models.BooleanField(u'Fabricar ?')
    fabricarQuantidade = models.IntegerField(u'Quantidade Fabricar')
    dataRecebimento = models.DateTimeField(u'Data de Recebimento', default=timezone.now)    

    def __unicode__(self):
        return "%s - %s" % (self.ordemServico.projetoNome, self.item.denominacao)
