from django.urls import path
from . import views

urlpatterns = [
    path('', views.painel_assuntos, name='painel'),
    path('tema/<int:tema_id>/', views.vitrine_eixo, name='vitrine'),
    path('recurso/<int:recurso_id>/', views.raio_x_recurso, name='detalhe'),
]
