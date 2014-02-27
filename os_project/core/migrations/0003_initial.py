# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pessoa'
        db.create_table(u'core_pessoa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'core', ['Pessoa'])

        # Adding model 'Cliente'
        db.create_table(u'core_cliente', (
            (u'pessoa_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Pessoa'], unique=True, primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(default='CLI', max_length=3)),
        ))
        db.send_create_signal(u'core', ['Cliente'])

        # Adding model 'OrdemServicoItem'
        db.create_table(u'core_ordemservicoitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('denominacao', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'core', ['OrdemServicoItem'])

        # Adding model 'OrdemServico'
        db.create_table(u'core_ordemservico', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('projetoNome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(related_name='os_cliente', to=orm['core.Cliente'])),
            ('numeroOP', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('equipamento', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('referencia', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('realizadoPor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='os_realizadopor', to=orm['core.Pessoa'])),
            ('realizadoData', self.gf('django.db.models.fields.DateTimeField')()),
            ('verificadoPor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='os_verificadopor', to=orm['core.Pessoa'])),
            ('verificadoData', self.gf('django.db.models.fields.DateTimeField')()),
            ('responsavel', self.gf('django.db.models.fields.related.ForeignKey')(related_name='os_responsavel', to=orm['core.Pessoa'])),
            ('revisao', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('revisaoData', self.gf('django.db.models.fields.DateTimeField')()),
            ('revisadoPor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='os_revisadopor', to=orm['core.Pessoa'])),
            ('entregaPrazo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('entregaLugar', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('totalConjunto', self.gf('django.db.models.fields.IntegerField')()),
            ('equipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Equipe'])),
        ))
        db.send_create_signal(u'core', ['OrdemServico'])

        # Adding model 'OrdemServico_OrdemServicoItem'
        db.create_table(u'core_ordemservico_ordemservicoitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ordemServico', self.gf('django.db.models.fields.related.ForeignKey')(related_name='osositem_os', to=orm['core.OrdemServico'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='osositem_item', to=orm['core.OrdemServicoItem'])),
            ('quantidade', self.gf('django.db.models.fields.IntegerField')()),
            ('acabamento', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('observacoes', self.gf('django.db.models.fields.TextField')()),
            ('fabricar', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fabricarQuantidade', self.gf('django.db.models.fields.IntegerField')()),
            ('dataRecebimento', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'core', ['OrdemServico_OrdemServicoItem'])

        # Adding model 'Equipe'
        db.create_table(u'core_equipe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'core', ['Equipe'])

        # Adding model 'Membro'
        db.create_table(u'core_membro', (
            (u'pessoa_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Pessoa'], unique=True, primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(default='MEM', max_length=3)),
            ('equipe', self.gf('django.db.models.fields.related.ForeignKey')(related_name='membro_equipe', to=orm['core.Equipe'])),
        ))
        db.send_create_signal(u'core', ['Membro'])


    def backwards(self, orm):
        # Deleting model 'Pessoa'
        db.delete_table(u'core_pessoa')

        # Deleting model 'Cliente'
        db.delete_table(u'core_cliente')

        # Deleting model 'OrdemServicoItem'
        db.delete_table(u'core_ordemservicoitem')

        # Deleting model 'OrdemServico'
        db.delete_table(u'core_ordemservico')

        # Deleting model 'OrdemServico_OrdemServicoItem'
        db.delete_table(u'core_ordemservico_ordemservicoitem')

        # Deleting model 'Equipe'
        db.delete_table(u'core_equipe')

        # Deleting model 'Membro'
        db.delete_table(u'core_membro')


    models = {
        u'core.cliente': {
            'Meta': {'object_name': 'Cliente', '_ormbases': [u'core.Pessoa']},
            u'pessoa_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Pessoa']", 'unique': 'True', 'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'default': "'CLI'", 'max_length': '3'})
        },
        u'core.equipe': {
            'Meta': {'object_name': 'Equipe'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.membro': {
            'Meta': {'object_name': 'Membro', '_ormbases': [u'core.Pessoa']},
            'equipe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'membro_equipe'", 'to': u"orm['core.Equipe']"}),
            u'pessoa_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Pessoa']", 'unique': 'True', 'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'default': "'MEM'", 'max_length': '3'})
        },
        u'core.ordemservico': {
            'Meta': {'object_name': 'OrdemServico'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'os_cliente'", 'to': u"orm['core.Cliente']"}),
            'entregaLugar': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'entregaPrazo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'equipamento': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'equipe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Equipe']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'numeroOP': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'projetoNome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'realizadoData': ('django.db.models.fields.DateTimeField', [], {}),
            'realizadoPor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'os_realizadopor'", 'to': u"orm['core.Pessoa']"}),
            'referencia': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'responsavel': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'os_responsavel'", 'to': u"orm['core.Pessoa']"}),
            'revisadoPor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'os_revisadopor'", 'to': u"orm['core.Pessoa']"}),
            'revisao': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'revisaoData': ('django.db.models.fields.DateTimeField', [], {}),
            'totalConjunto': ('django.db.models.fields.IntegerField', [], {}),
            'verificadoData': ('django.db.models.fields.DateTimeField', [], {}),
            'verificadoPor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'os_verificadopor'", 'to': u"orm['core.Pessoa']"})
        },
        u'core.ordemservico_ordemservicoitem': {
            'Meta': {'object_name': 'OrdemServico_OrdemServicoItem'},
            'acabamento': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'dataRecebimento': ('django.db.models.fields.DateTimeField', [], {}),
            'fabricar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fabricarQuantidade': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'osositem_item'", 'to': u"orm['core.OrdemServicoItem']"}),
            'observacoes': ('django.db.models.fields.TextField', [], {}),
            'ordemServico': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'osositem_os'", 'to': u"orm['core.OrdemServico']"}),
            'quantidade': ('django.db.models.fields.IntegerField', [], {})
        },
        u'core.ordemservicoitem': {
            'Meta': {'object_name': 'OrdemServicoItem'},
            'denominacao': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.pessoa': {
            'Meta': {'object_name': 'Pessoa'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['core']