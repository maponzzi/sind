from django.contrib import admin
from models import *
#from models import Tema, TipoArt, Articulo, TipoBanner, Banner, Seccion
#from sorl.thumbnail.admin import AdminImageMixin


class ArticuloAdmin(admin.ModelAdmin):
	exclude = ('Slug', 'Visitas',)
	filter_horizontal = ('Temas',)


admin.site.register(Tema)
admin.site.register(TipoArt)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(TipoBanner)
admin.site.register(Banner)