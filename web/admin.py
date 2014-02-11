from django.contrib import admin
from models import Tema, TipoArt, Articulo, TipoBanner, Banner


class ArticuloAdmin(admin.ModelAdmin):
	exclude = ('Mes', 'Anio', 'Slug',)
	filter_horizontal = ('Temas',)


admin.site.register(Tema)
admin.site.register(TipoArt)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(TipoBanner)
admin.site.register(Banner)