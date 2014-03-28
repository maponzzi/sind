from . import models
from django.shortcuts import render
from django.views.generic import TemplateView
import datetime


def home(request):
	fecha = datetime.datetime.now()
	mes = fecha.month
	anio = fecha.year
	template = "index.html"
	banners = models.Banner.objects.order_by('pk')
	articulos = models.Articulo.objects.filter(mes=mes, anio=anio)
	secciones = models.Articulo.objects.filter(tipo__sub=4, stt=True).order_by('orden')


	Principal = {"banners": banners, }
	return render(request, template, locals())


class ArticuloView(TemplateView):
	model = models.Articulo
	template_name = "interior.html"

	def get_context_data(self, **kwargs):
		context = super(ArticuloView, self).get_context_data(**kwargs)
		context['articulo'] = self.model.objects.filter(slug=context['slug'])
		return context


def test(request):
	pass