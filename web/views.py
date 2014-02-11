from django.shortcuts import render
from django.views.generic import TemplateView
from . import models


def home(request):
	template = "index.html"
	return render(request, template)

	
class ArticuloView(TemplateView):
	model = models.Articulo
	template_name = "Interior.html"

	def get_context_data(self, **kwargs):
		context = super(ArticuloView, self).get_context_data(**kwargs)
		context['articulo'] = self.model.objects.filter(Slug=context['slug'])
		return context


def test(request):
	pass