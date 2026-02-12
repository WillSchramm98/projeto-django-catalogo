from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Questao, Alternativa


def index(request):
    questoes = Questao.objects.all()
    return render(request, 'enquetes/index.html', {'questoes': questoes})


def detalhes(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'enquetes/detalhes.html', {'questao': questao})


def voto(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        selecionada = questao.alternativa_set.get(pk=request.POST['alternativa'])
    except (KeyError, Alternativa.DoesNotExist):
        return render(request, 'enquetes/detalhes.html', {
            'questao': questao,
            'error_message': "Você não selecionou uma opção válida.",
        })
    else:
        selecionada.votos = F('votos') + 1
        selecionada.save()
        return HttpResponseRedirect(
            reverse('enquetes:resultados', args=(questao.id,))
        )


def resultados(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'enquetes/resultados.html', {'questao': questao})
