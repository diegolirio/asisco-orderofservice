# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'OrdemServico.entregaLugar'
        db.alter_column(u'core_ordemservico', 'entregaLugar', self.gf('django.db.models.fields.CharField')(max_length=250))

    def backwards(self, orm):

        # Changing field 'OrdemServico.entregaLugar'
        db.alter_column(u'core_ordemservico', 'entregaLugar', self.gf('django.db.models.fields.TextField')())

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