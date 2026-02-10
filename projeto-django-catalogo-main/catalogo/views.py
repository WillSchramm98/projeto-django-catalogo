from django.shortcuts import render, get_object_or_404
from .models import Tema, Recurso


def painel_assuntos(request):
    temas = Tema.objects.all()
    return render(request, 'catalogo/painel.html', {'temas': temas})


def vitrine_eixo(request, tema_id):
    tema = get_object_or_404(Tema, id=tema_id)
    recursos = tema.recurso_set.order_by('-prestigio')
    return render(request, 'catalogo/vitrine.html', {
        'tema': tema,
        'recursos': recursos
    })


def raio_x_recurso(request, recurso_id):
    recurso = get_object_or_404(Recurso, id=recurso_id)
    return render(request, 'catalogo/detalhe.html', {'recurso': recurso})
