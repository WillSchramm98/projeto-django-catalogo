from django.shortcuts import render, get_object_or_404
from .models import Tema, Recurso
from django.db.models import F
from django.shortcuts import redirect
from .forms import TemaForm
from .forms import RecursoForm

def excluir_recurso(request, recurso_id):
    recurso = get_object_or_404(Recurso, pk=recurso_id)
    if request.method == 'POST':
        recurso.delete()
        return redirect('painel')
    return render(request, 'catalogo/confirmar_exclusao.html', {'recurso': recurso})

def editar_recurso(request, recurso_id):
    recurso = Recurso.objects.get(pk=recurso_id)

    if request.method == 'POST':
        form = RecursoForm(request.POST, instance=recurso)
        if form.is_valid():
            form.save()
            return redirect('detalhe', recurso_id=recurso.id)
    else:
        form = RecursoForm(instance=recurso)

    return render(request, 'catalogo/form.html', {'form': form})

def adicionar_recurso(request):
    if request.method == 'POST':
        form = RecursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('painel')
    else:
        form = RecursoForm()

    return render(request, 'catalogo/form.html', {'form': form})

def adicionar_tema(request):
    if request.method == 'POST':
        form = TemaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('painel')
    else:
        form = TemaForm()

    return render(request, 'catalogo/form.html', {'form': form})


def painel(request):
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


def curtir_recurso(request, recurso_id):
    recurso = Recurso.objects.get(pk=recurso_id)
    recurso.prestigio = F('prestigio') + 1
    recurso.save()
    return redirect('detalhe', recurso_id=recurso.id)