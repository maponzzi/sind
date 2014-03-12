# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Articulo.Actualizado'
        db.add_column(u'web_articulo', 'Actualizado',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Articulo.Actualizado'
        db.delete_column(u'web_articulo', 'Actualizado')


    models = {
        u'web.articulo': {
            'Actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'Anio': ('django.db.models.fields.SmallIntegerField', [], {'default': '2014', 'blank': 'True'}),
            'Cifras': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'Contacto': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'Creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'Editor': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'Img1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Img2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ImgPortada': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Mes': ('django.db.models.fields.SmallIntegerField', [], {'default': '3', 'blank': 'True'}),
            'Meta': {'object_name': 'Articulo'},
            'NotaComp': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'Orden': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'PieImg1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'PieImg2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'Slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'blank': 'True'}),
            'Stt': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Sumario': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'Temas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['web.Tema']", 'symmetrical': 'False'}),
            'Tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.TipoArt']"}),
            'Titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '300'}),
            'TxtPrinc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'web.banner': {
            'Alt': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'Creado': ('django.db.models.fields.DateTimeField', [], {}),
            'Img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Banner'},
            'Nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Stt': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
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
            'Sub': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'web.tipobanner': {
            'Meta': {'object_name': 'TipoBanner'},
            'Nombre': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['web']