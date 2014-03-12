from django.db import models
# from django.db.models import Q
from django.template import defaultfilters
from datetime import date
from sorl.thumbnail import ImageField


class Tema(models.Model):
	Nombre = models.CharField(max_length=140, blank=True)

	def __unicode__(self):
		return self.Nombre


class TipoArt(models.Model):
	Nombre = models.CharField(max_length=50, blank=True)
	Sub = models.SmallIntegerField(blank=True, null=True)

	def __unicode__(self):
		return "%i. %s" % (self.id, self.Nombre)


class Articulo(models.Model):
	Titulo = models.CharField(max_length=300, unique=True, null=False)
	Sumario = models.CharField(max_length=300, blank=True)
	Editor = models.CharField(max_length=140, blank=True)
	NotaComp = models.TextField(blank=True)
	Cifras = models.TextField(blank=True)
	Contacto = models.TextField(blank=True)
	PieImg1 = models.CharField(max_length=255, blank=True)
	PieImg2 = models.CharField(max_length=255, blank=True)
	Img1 = models.ImageField(upload_to='img/notas/', blank=True, null=True)
	Img2 = models.ImageField(upload_to='img/notas/', blank=True, null=True)
	ImgPortada = models.ImageField(upload_to='img/portada/', blank=True, null=True)
	Tipo = models.ForeignKey(TipoArt)
	Orden = models.SmallIntegerField(default=0)
	Mes = models.SmallIntegerField(blank=True, default=date.today().month)
	Anio = models.SmallIntegerField(blank=True, default=date.today().year)
	Slug = models.SlugField(max_length=255, blank=True)
	Temas = models.ManyToManyField(Tema)
	Creado = models.DateTimeField(auto_now_add=True)
	Actualizado = models.DateTimeField(auto_now=True, null=True)
	Visitas = models.IntegerField(default=0)
	Stt = models.NullBooleanField()

	def save(self, *args, **kwargs):
		# fecha = date.today()
		# self.Mes = fecha.month
		# self.Anio = fecha.year
		self.Slug = defaultfilters.slugify(self.Titulo)#self.Titulo.lower().replace(' ', '-')
		super(Articulo, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.Titulo


class TipoBanner(models.Model):
	Nombre = models.CharField(max_length=50, blank=True)

	def __unicode__(self):
		return "%i. %s" % (self.id, self.Nombre)


class Banner(models.Model):
	Nombre = models.CharField(max_length=50)
	Alt = models.TextField(blank=True)
	Img = models.ImageField(upload_to='img/banners/', blank=True, null=True)
	Tipo = models.ForeignKey(TipoBanner)
	Creado = models.DateTimeField()
	Link = models.URLField(blank=True, null=True)
	Stt = models.BooleanField(default=True)

	def __unicode__(self):
		return self.Nombre