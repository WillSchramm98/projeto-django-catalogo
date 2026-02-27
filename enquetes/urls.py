from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'enquetes'

router = routers.DefaultRouter()
router.register(r'questoes', views.QuestaoViewSet, basename='questao')

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:questao_id>/', views.detalhes, name='detalhes'),
    path('<int:questao_id>/voto/', views.voto, name='voto'),
    path('<int:questao_id>/resultados/', views.resultados, name='resultados'),
    path('api/', include(router.urls)),
]
