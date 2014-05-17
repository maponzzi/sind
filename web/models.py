from django.db import models
# from django.db.models import Q
from django.template import defaultfilters
from datetime import date
from sorl.thumbnail import ImageField


class Estado(models.Model):
	nombre = models.CharField(max_length=140, blank=True, null=True)
	color = models.CharField(max_length=10, blank=True)
	slug = models.SlugField(max_length=50, blank=True)

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.nombre)
		super(Estado, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombre


class Industria(models.Model):
	edo = models.ForeignKey(Estado)
	anio = models.SmallIntegerField(blank=True, null=True)
	empresa = models.CharField(max_length=140, blank=True, null=True)
	locacion = models.CharField(max_length=300, blank=True, null=True)
	cd = models.CharField(max_length=60, blank=True, null=True)
	superficie = models.IntegerField(blank=True, null=True)
	sector = models.CharField(max_length=60, blank=True, null=True)
	origen = models.CharField(max_length=60, blank=True, null=True)
	tipo = models.CharField(max_length=30, blank=True, null=True)

	def __unicode__(self):
		return self.empresa

		
class Tema(models.Model):
	nombre = models.CharField(max_length=140, blank=True)

	def __unicode__(self):
		return self.nombre


class TipoArt(models.Model):
	nombre = models.CharField(max_length=50, blank=True)
	sub = models.SmallIntegerField(blank=True, null=True)

	def __unicode__(self):
		return "%i. %s" % (self.id, self.nombre)


class Articulo(models.Model):
	titulo = models.CharField(max_length=300, null=False)
	sumario = models.CharField(max_length=300, blank=True, null=True)
	editor = models.CharField(max_length=140, blank=True, null=True)
	contenido = models.TextField(blank=True)
	cifras = models.TextField(blank=True, null=True)
	contacto = models.TextField(blank=True, null=True)
	pieimg1 = models.TextField(blank=True, null=True)
	pieimg2 = models.TextField(blank=True, null=True)
	img1 = models.ImageField(upload_to='img/notas/', blank=True, null=True)
	img2 = models.ImageField(upload_to='img/notas/', blank=True, null=True)
	imgportada = models.ImageField(upload_to='img/portada/', blank=True, null=True)
	tipo = models.ForeignKey(TipoArt)
	orden = models.SmallIntegerField(default=0, null=True)
	mes = models.SmallIntegerField(blank=True, default=date.today().month)
	anio = models.SmallIntegerField(blank=True, default=date.today().year)
	slug = models.SlugField(max_length=255, blank=True, null=True)
	temas = models.ManyToManyField(Tema)
	creado = models.DateTimeField(auto_now_add=True, null=True)
	actualizado = models.DateTimeField(auto_now=True, null=True)
	visitas = models.IntegerField(default=0, null=True)
	stt = models.NullBooleanField()

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.titulo)#self.Titulo.lower().replace(' ', '-')
		super(Articulo, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.titulo


class TipoBanner(models.Model):
	nombre = models.CharField(max_length=50, blank=True)

	def __unicode__(self):
		return "%i. %s" % (self.id, self.nombre)


class Banner(models.Model):
	nombre = models.CharField(max_length=50)
	alt = models.TextField(blank=True)
	img = models.ImageField(upload_to='img/banners/', blank=True, null=True)
	tipo = models.ForeignKey(TipoBanner)
	creado = models.DateTimeField(auto_now_add=True, null=True)
	link = models.URLField(blank=True, null=True)
	stt = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre


class Solicitante(models.Model):
	nombre = models.CharField(max_length=250, blank=True)
	requisitos = models.TextField(blank=True, null=True)
	contacto = models.CharField(max_length=250, blank=True, null=True)
	estado = models.ForeignKey(Estado)

	def __unicode__(self):
		return self.nombre


class Requerimiento(models.Model):
	solicita = models.ForeignKey(Solicitante)
	desc = models.TextField(blank=True)

	def __unicode__(self):
		return self.desc