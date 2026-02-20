from django.urls import path
from . import views

urlpatterns = [
    path('', views.painel_assuntos, name='painel'),
    path('tema/<int:tema_id>/', views.vitrine_eixo, name='vitrine'),
    path('recurso/<int:recurso_id>/', views.raio_x_recurso, name='detalhe'),
    path('recurso/<int:recurso_id>/curtir/', views.curtir_recurso, name='curtir'),
    path('tema/adicionar/', views.adicionar_tema, name='adicionar_tema'),
    path('recurso/adicionar/', views.adicionar_recurso, name='adicionar_recurso'),
    path('recurso/<int:recurso_id>/editar/', views.editar_recurso, name='editar_recurso'),
    path('recurso/<int:recurso_id>/excluir/', views.excluir_recurso, name='excluir_recurso'),
]
