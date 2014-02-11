from django.db import models
from django.db.models import Q
from django.template import defaultfilters
from datetime import date

class Tema(models.Model):
	Nombre = models.CharField(max_length=140, blank=True)

	def __unicode__(self):
		return self.Nombre


class TipoArt(models.Model):
	Nombre = models.CharField(max_length=50, blank=True)

	def __unicode__(self):
		return self.Nombre


class Articulo(models.Model):
	Titulo = models.CharField(max_length=300, unique=True, null=False)
	Sumario = models.CharField(max_length=300, blank=True)
	Editor = models.CharField(max_length=140, blank=True)
	NotaComp = models.TextField(blank=True)
	Cifras = models.TextField(blank=True)
	Contacto = models.TextField(blank=True)
	PieImg1 = models.CharField(max_length=255, blank=True)
	PieImg2 = models.CharField(max_length=255, blank=True)
	Img1 = models.ImageField(upload_to='Img/Notas/', blank=True, null=True)
	Img2 = models.ImageField(upload_to='Img/Notas/', blank=True, null=True)
	ImgPortada = models.ImageField(upload_to='Img/Portada/', blank=True, null=True)
	Tipo = models.ForeignKey(TipoArt)
	OrdenCol = models.SmallIntegerField(default=0)
	Mes = models.SmallIntegerField(blank=True)
	Anio = models.SmallIntegerField(blank=True)
	Slug = models.SlugField(max_length=255, blank=True)
	Temas = models.ManyToManyField(Tema)
	Creado = models.DateTimeField(auto_now_add=True)
	mitest = models.CharField(max_length=140, blank=True)
	otrocampo = models.CharField(max_length=120, blank=True)

	def save(self, *args, **kwargs):
		fecha = date.today()
		self.Mes = fecha.month
		self.Anio = fecha.year
		self.Slug = defaultfilters.slugify(self.Titulo)#self.Titulo.lower().replace(' ', '-')
		super(Articulo, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.Titulo


class TipoBanner(models.Model):
	Nombre = models.CharField(max_length=50, blank=True)

	def __unicode__(self):
		return self.Nombre


class Banner(models.Model):
	Nombre = models.CharField(max_length=50)
	Alt = models.TextField(blank=True)
	Img = models.ImageField(upload_to='Img/Banners/', blank=False, null=False)
	Tipo = models.ForeignKey(TipoBanner)
	Creado = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.Nombre