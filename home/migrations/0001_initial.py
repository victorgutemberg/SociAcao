# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Usuario'
        db.create_table('home_usuario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('sobrenome', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('link_facebook', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('home', ['Usuario'])

        # Adding model 'Camisa'
        db.create_table('home_camisa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('foto', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('home', ['Camisa'])

        # Adding model 'Compra'
        db.create_table('home_compra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Usuario'])),
            ('data', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('home', ['Compra'])

        # Adding M2M table for field itens on 'Compra'
        db.create_table('home_compra_itens', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('compra', models.ForeignKey(orm['home.compra'], null=False)),
            ('camisa', models.ForeignKey(orm['home.camisa'], null=False))
        ))
        db.create_unique('home_compra_itens', ['compra_id', 'camisa_id'])


    def backwards(self, orm):
        # Deleting model 'Usuario'
        db.delete_table('home_usuario')

        # Deleting model 'Camisa'
        db.delete_table('home_camisa')

        # Deleting model 'Compra'
        db.delete_table('home_compra')

        # Removing M2M table for field itens on 'Compra'
        db.delete_table('home_compra_itens')


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
            'itens': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['home.Camisa']", 'symmetrical': 'False'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Usuario']"})
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