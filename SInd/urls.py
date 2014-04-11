from django.conf.urls import patterns, include, url
from web import views

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'web.views.home', name='home'),
    url(r'^articulo/(?P<slug>[^/]+)/$', views.ArticuloView.as_view(), name='articulo'),
    url(r'^empresa/$', 'web.views.empresa', name='empresa'),
    url(r'^se-buscan-proveedores/(?P<slug>[^/]+)/$', views.ProveedoresView.as_view(), name="proveedores"),
    url(r'^nuevas-industrias/(?P<slug>[^/]+)/$', views.IndustriasView.as_view(), name="industrias"),
    # url(r'^SInd/', include('SInd.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
