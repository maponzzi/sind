# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tema'
        db.create_table(u'web_tema', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nombre', self.gf('django.db.models.fields.CharField')(max_length=140, blank=True)),
        ))
        db.send_create_signal(u'web', ['Tema'])

        # Adding model 'TipoArt'
        db.create_table(u'web_tipoart', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nombre', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'web', ['TipoArt'])

        # Adding model 'Articulo'
        db.create_table(u'web_articulo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Titulo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=300)),
            ('Sumario', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('Editor', self.gf('django.db.models.fields.CharField')(max_length=140, blank=True)),
            ('NotaComp', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('Cifras', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('Contacto', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('PieImg1', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('PieImg2', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('Img1', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('Img2', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('ImgPortada', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('Tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.TipoArt'])),
            ('OrdenCol', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('Mes', self.gf('django.db.models.fields.SmallIntegerField')(blank=True)),
            ('Anio', self.gf('django.db.models.fields.SmallIntegerField')(blank=True)),
            ('Slug', self.gf('django.db.models.fields.SlugField')(max_length=255, blank=True)),
            ('Creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('mitest', self.gf('django.db.models.fields.CharField')(max_length=140, blank=True)),
            ('otrocampo', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
        ))
        db.send_create_signal(u'web', ['Articulo'])

        # Adding M2M table for field Temas on 'Articulo'
        m2m_table_name = db.shorten_name(u'web_articulo_Temas')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('articulo', models.ForeignKey(orm[u'web.articulo'], null=False)),
            ('tema', models.ForeignKey(orm[u'web.tema'], null=False))
        ))
        db.create_unique(m2m_table_name, ['articulo_id', 'tema_id'])

        # Adding model 'TipoBanner'
        db.create_table(u'web_tipobanner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nombre', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'web', ['TipoBanner'])

        # Adding model 'Banner'
        db.create_table(u'web_banner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Alt', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('Img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('Tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.TipoBanner'])),
            ('Creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['Banner'])


    def backwards(self, orm):
        # Deleting model 'Tema'
        db.delete_table(u'web_tema')

        # Deleting model 'TipoArt'
        db.delete_table(u'web_tipoart')

        # Deleting model 'Articulo'
        db.delete_table(u'web_articulo')

        # Removing M2M table for field Temas on 'Articulo'
        db.delete_table(db.shorten_name(u'web_articulo_Temas'))

        # Deleting model 'TipoBanner'
        db.delete_table(u'web_tipobanner')

        # Deleting model 'Banner'
        db.delete_table(u'web_banner')


    models = {
        u'web.articulo': {
            'Anio': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True'}),
            'Cifras': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'Contacto': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'Creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'Editor': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'Img1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Img2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ImgPortada': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Mes': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True'}),
            'Meta': {'object_name': 'Articulo'},
            'NotaComp': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'OrdenCol': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'PieImg1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'PieImg2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'Slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'blank': 'True'}),
            'Sumario': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'Temas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['web.Tema']", 'symmetrical': 'False'}),
            'Tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.TipoArt']"}),
            'Titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mitest': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'otrocampo': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'})
        },
        u'web.banner': {
            'Alt': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'Creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'Img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'Meta': {'object_name': 'Banner'},
            'Nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.TipoBanner']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'web.tema': {
            'Meta': {'object_name': 'Tema'},
            'Nombre': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'web.tipoart': {
            'Meta': {'object_name': 'TipoArt'},
            'Nombre': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'web.tipobanner': {
            'Meta': {'object_name': 'TipoBanner'},
            'Nombre': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['web']