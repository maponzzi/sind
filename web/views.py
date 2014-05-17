from . import models
from django.shortcuts import render
from django.views.generic import TemplateView
import datetime


def home(request):
	num_avances = 12
	fecha = datetime.datetime.now()
	mes = fecha.month
	anio = fecha.year
	mesactual = 3
	template = "index.html"

	banners = models.Banner.objects.order_by('pk')
	secciones = models.Articulo.objects.filter(tipo__sub=4, stt=True).order_by('orden')
	arts = models.Articulo.objects.filter(mes=mesactual, anio=anio).exclude(tipo__sub=4).order_by('-orden')
	avances = arts[:num_avances]
	portada = arts[len(arts)-1:]
	articulos = arts[num_avances:len(arts)-1]

	tema1 = models.Articulo.objects.filter(temas=1).exclude(mes=mesactual, anio=anio).exclude(tipo__sub=4, stt=True).order_by('-anio', '-mes')[:6]
	tema2 = models.Articulo.objects.filter(temas=5).exclude(mes=mesactual, anio=anio).exclude(tipo__sub=4, stt=True).order_by('-anio', '-mes')[:6]

	#Principal = {"banners": banners, }
	return render(request, template, locals())


class ArticuloView(TemplateView):
	model = models.Articulo
	template_name = "interior.html"

	def get_context_data(self, **kwargs):
		context = super(ArticuloView, self).get_context_data(**kwargs)
		miArticulo = self.model.objects.filter(slug=context['slug'])
		miFecha = datetime.date(miArticulo[0].anio, miArticulo[0].mes, 1)

		context['articulo'] = miArticulo
		context['fecha'] = {'miFecha': miFecha}
		return context


class IndustriasView(TemplateView):
	model = models.Industria
	model1 = models.Estado
	template_name = "industrias.html"

	def get_context_data(self, **kwargs):
		fecha = datetime.datetime.now()
		anio = fecha.year
		mirango = range(2009, anio) #[2009, 2010, 2011]
		context = super(IndustriasView, self).get_context_data(**kwargs)
		industrias = self.model.objects.filter(edo__slug=context['slug']).order_by('-anio', 'id')
		estados = self.model1.objects.all()

		context['anios'] = mirango
		context['industrias'] = industrias
		context['estados'] = estados
		return context


class ProveedoresView(TemplateView):
	model1 = models.Solicitante
	model2 = models.Requerimiento
	model3 = models.Estado
	template_name = "proveedores.html"

	def get_context_data(self, **kwargs):
		context = super(ProveedoresView, self).get_context_data(**kwargs)
		solicitantes = self.model1.objects.filter(estado__slug=context['slug'])
		requerimientos = self.model2.objects.filter(solicita__estado__slug=context['slug'])
		estados = self.model3.objects.all().order_by('pk')

		context['solicitantes'] = solicitantes
		context['requerimientos'] = requerimientos
		context['estados'] = estados
		return context


def empresa(request):
	template = "empresa.html"
	return render(request, template)


def test(request):
	pass