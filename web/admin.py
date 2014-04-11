from django.contrib import admin
from models import *
#from models import Tema, TipoArt, Articulo, TipoBanner, Banner, Seccion
#from sorl.thumbnail.admin import AdminImageMixin


class ArticuloAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'tipo', 'mes', 'anio', 'orden', 'img1', 'actualizado')
	list_filter = ('tipo', 'tipo__sub')
	exclude = ('slug', 'visitas',)
	filter_horizontal = ('temas',)


class BannerAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'tipo', 'img', 'link')


class EstadoAdmin(admin.ModelAdmin):
	exclude = ('slug',)


admin.site.register(Estado, EstadoAdmin)
admin.site.register(Industria)
admin.site.register(Tema)
admin.site.register(TipoArt)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(TipoBanner)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Solicitante)
admin.site.register(Requerimiento)
