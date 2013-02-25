# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table('home_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('camisa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Camisa'])),
            ('quantidade', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('home', ['Item'])


    def backwards(self, orm):
        # Deleting model 'Item'
        db.delete_table('home_item')


    models = {
        'home.camisa': {
            'Meta': {'object_name': 'Camisa'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'foto': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'home.compra': {
            'Meta': {'object_name': 'Compra'},
            'data': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itens': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['home.Item']", 'symmetrical': 'False'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Usuario']"})
        },
        'home.item': {
            'Meta': {'object_name': 'Item'},
            'camisa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Camisa']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantidade': ('django.db.models.fields.IntegerField', [], {})
        },
        'home.usuario': {
            'Meta': {'object_name': 'Usuario'},
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_facebook': ('django.db.models.fields.TextField', [], {}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sobrenome': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['home']