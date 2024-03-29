from django.conf.urls import patterns, include, url
from django.contrib import admin
# Uncomment the next two lines to enable the admin:


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^alumnos/$','principal.views.lista_alumnos'),
    url(r'^dato-alumno/(?P<id_alumno>\d+)$','principal.views.dato_alumno'),
    url(r'^dato-curso/(?P<id_curso>\d+)$','principal.views.dato_curso'),
    url(r'^dato-profesor/(?P<id_profesor>\d+)$','principal.views.dato_profesor'),
    url(r'^cursos/$','principal.views.lista_cursos'),
    url(r'^profesores/$','principal.views.lista_profesores'),
    url(r'^dato-alumno/nuevo/$','principal.views.nuevo_alumno'),
    url(r'^nuevocur/$','principal.views.nuevo_curso'),
    url(r'^nuevoprof/$','principal.views.nuevo_profesor'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contactenos/$', 'principal.views.contacto'),
    url(r'^matriculas/$', 'principal.views.nueva_matricula'),
)
