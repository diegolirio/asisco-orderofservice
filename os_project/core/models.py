# coding: utf-8
from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nome

class OrdemServico(models.Model):
    numero = models.CharField(u'Ordem de Serviço', max_length=50)
    projetoNome = models.CharField(u'Nome do Projeto', max_length=100)
    cliente = models.ForeignKey(Pessoa, verbose_name=u'Cliente', related_name='os_cliente')
    numeroOP = models.CharField(u'Nº.OP', max_length=20)
    equipamento = models.CharField(max_length=100)
    referencia = models.CharField(u'Referencia/Nº de Desenho', max_length=100)
    realizadoPor = models.ForeignKey(Pessoa, verbose_name=u'Realizado Por', related_name='os_realizadopor')
    realizadoData = models.DateTimeField(u'Data Realizado')
    verificadoPor = models.ForeignKey(Pessoa, verbose_name=u'Verificado Por', related_name='os_verificadopor')
    verificadoData = models.DateTimeField(u'Data Verificado')
    responsavel = models.ForeignKey(Pessoa, verbose_name=u'Responsavel Projeto', related_name='os_responsavel')
    revisao = models.CharField(u'Revisão', max_length=20)
    revisaoData = models.DateTimeField(u'Data da Revisão')
    revisadoPor = models.ForeignKey(Pessoa, verbose_name=u'Revisado Por', related_name='os_revisadopor')
    entregaPrazo = models.CharField(u'Prazo de Entrega', max_length=50)
    entregaLugar = models.TextField(u'Lugar de Entrega')
    totalConjunto = models.IntegerField(u'Total de Conjuntos')

class OrdemServicoItem(models.Model):
    numero = models.CharField(u'Numero de Desenvo/Conjunto/Peça', max_length=100) 
    denominacao = models.CharField(u'Denominação', max_length=200)
    ordemServico = models.ManyToManyField(OrdemServico, through='Os_OsItem')

    def __unicode__(self):
        "%s - %s" % (self.numero, self.denominacao)

class Equipe(models.Model):
    nome = models.CharField('Nome da Equipe', max_length=100)
    membro = models.ManyToManyField(Pessoa, through='Equipe_Membro', related_name='equipe_membro')

    def __unicode__(self):
        return self.nome

class Equipe_Membro(models.Model):
    """
    Criei essa tabela N x N separada pensando em possibilitar um membro fazer parte de N equipes
        e se precisar criar campos especificos por exemplo: 
            status(Ativo/Excluido)    
            função, etc...
    """
    membro = models.ForeignKey(Pessoa, related_name='equipemembro_membro')
    equipe = models.ForeignKey(Equipe, related_name='equipemembro_equipe')

class Os_OsItem(models.Model):
    ordemServico = models.ForeignKey(OrdemServico, related_name='osositem_os')
    item = models.ForeignKey(OrdemServicoItem, related_name='osositem_item')
    quantidade = models.IntegerField()
    acabamento = models.CharField(u'Acabamento/RAL', max_length=100)
    observacoes = models.TextField(u'Observações')
    fabricar = models.BooleanField(u'Fabricar ?')
    fabricarQuantidade = models.IntegerField(u'Quantidade Fabricar')
    dataRecebimento = models.DateTimeField(u'Data de Recebimento')
    equipe = models.ForeignKey(Equipe)

    def __unicode__(self):
        return "%s - %s" % (self.ordemServico.projetoNome, self.item.denominacao)



