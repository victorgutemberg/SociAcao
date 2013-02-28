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
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('celular', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Celular'])),
            ('link_facebook', self.gf('django.db.models.fields.TextField')()),
            ('ciente', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('home', ['Usuario'])

        # Adding model 'Celular'
        db.create_table('home_celular', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('operadora', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Operadora'])),
        ))
        db.send_create_signal('home', ['Celular'])

        # Adding model 'Operadora'
        db.create_table('home_operadora', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('home', ['Operadora'])

        # Adding model 'Camisa'
        db.create_table('home_camisa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('foto', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('home', ['Camisa'])

        # Adding model 'Item'
        db.create_table('home_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('camisa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Camisa'])),
            ('quantidade', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('home', ['Item'])

        # Adding model 'FormaPagamento'
        db.create_table('home_formapagamento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('home', ['FormaPagamento'])

        # Adding model 'Compra'
        db.create_table('home_compra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Usuario'])),
            ('data', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('formaPagamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.FormaPagamento'])),
            ('pago', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('entregue', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('home', ['Compra'])

        # Adding M2M table for field itens on 'Compra'
        db.create_table('home_compra_itens', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('compra', models.ForeignKey(orm['home.compra'], null=False)),
            ('item', models.ForeignKey(orm['home.item'], null=False))
        ))
        db.create_unique('home_compra_itens', ['compra_id', 'item_id'])


    def backwards(self, orm):
        # Deleting model 'Usuario'
        db.delete_table('home_usuario')

        # Deleting model 'Celular'
        db.delete_table('home_celular')

        # Deleting model 'Operadora'
        db.delete_table('home_operadora')

        # Deleting model 'Camisa'
        db.delete_table('home_camisa')

        # Deleting model 'Item'
        db.delete_table('home_item')

        # Deleting model 'FormaPagamento'
        db.delete_table('home_formapagamento')

        # Deleting model 'Compra'
        db.delete_table('home_compra')

        # Removing M2M table for field itens on 'Compra'
        db.delete_table('home_compra_itens')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'home.camisa': {
            'Meta': {'object_name': 'Camisa'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'foto': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'home.celular': {
            'Meta': {'object_name': 'Celular'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'operadora': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Operadora']"})
        },
        'home.compra': {
            'Meta': {'object_name': 'Compra'},
            'data': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'entregue': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'formaPagamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.FormaPagamento']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itens': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['home.Item']", 'symmetrical': 'False'}),
            'pago': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Usuario']"})
        },
        'home.formapagamento': {
            'Meta': {'object_name': 'FormaPagamento'},
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'home.item': {
            'Meta': {'object_name': 'Item'},
            'camisa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Camisa']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantidade': ('django.db.models.fields.IntegerField', [], {})
        },
        'home.operadora': {
            'Meta': {'object_name': 'Operadora'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'home.usuario': {
            'Meta': {'object_name': 'Usuario'},
            'celular': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Celular']"}),
            'ciente': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_facebook': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['home']