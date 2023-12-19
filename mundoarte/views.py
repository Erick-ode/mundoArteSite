from django.shortcuts import render
from mundoarte.models import Produto


def index(request):
    produtos = Produto.objects.filter(publicada=True)
    return render(request, 'mundoarte/index.html', {"produtos": produtos})


def buscar(request):
    produtos = Produto.objects.filter(publicada=True)

    if 'buscar' in request.GET:
        valor_a_buscar = request.GET['buscar']
        if valor_a_buscar:
            produtos = produtos.filter(nome__icontains=valor_a_buscar)

    return render(request, 'mundoarte/index.html', {'produtos': produtos})


def ordenarPorNome(request):
    produtos = Produto.objects.order_by('nome').filter(publicada=True)

    return render(request, 'mundoarte/index.html', {'produtos': produtos})


def ordenarPorPrecoCrescente(request):
    produtos = Produto.objects.order_by('preco').filter(publicada=True)

    return render(request, 'mundoarte/index.html', {'produtos': produtos})


def ordenarPorPrecoDescendente(request):
    produtos = Produto.objects.order_by('-preco').filter(publicada=True)

    return render(request, 'mundoarte/index.html', {'produtos': produtos})


def sobre(request):
    return render(request, 'mundoarte/info/sobre.html')


def endereco(request):
    return render(request, 'mundoarte/info/endereco.html')


def redesSociais(request):
    return render(request, 'mundoarte/info/redes-sociais.html')