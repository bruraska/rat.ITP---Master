from datetime import datetime
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',

    url(r'^$', 'app.views.pagina_inicial', name='pagina_inicial'),

    url(r'^listar_aluno', 'app.views.listar_aluno', name='listar_aluno'),
    url(r'^novo_aluno', 'app.views.novo_aluno', name='novo_aluno'),
    url(r'^editar_aluno/(?P<pk>\d+)$', 'app.views.editar_aluno', name='editar_aluno'),
    url(r'^apagar_aluno/(?P<pk>\d+)$', 'app.views.apagar_aluno', name='apagar_aluno'),
)
