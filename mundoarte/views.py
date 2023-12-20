from django.shortcuts import render
from mundoarte.models import Produto, Categoria, Subcategoria


categorias = Categoria.objects.all()
subcategorias = Subcategoria.objects.all()


def index(request):
    produtos = Produto.objects.filter(publicada=True)

    return render(request, 'mundoarte/index.html', {'produtos': produtos, 'categorias': categorias, 'subcategorias': subcategorias})


def buscar(request):
    produtos = Produto.objects.filter(publicada=True)

    if 'buscar' in request.GET:
        valor_a_buscar = request.GET['buscar']
        if valor_a_buscar:
            produtos = produtos.filter(nome__icontains=valor_a_buscar)

    return render(request, 'mundoarte/index.html', {'produtos': produtos, 'categorias': categorias, 'subcategorias': subcategorias})


def ordenarPorNome(request):
    produtos = Produto.objects.order_by('nome').filter(publicada=True)

    return render(request, 'mundoarte/index.html', {'produtos': produtos, 'categorias': categorias, 'subcategorias': subcategorias})


def ordenarPorPrecoCrescente(request):
    produtos = Produto.objects.order_by('preco').filter(publicada=True)

    return render(request, 'mundoarte/index.html', {'produtos': produtos, 'categorias': categorias, 'subcategorias': subcategorias})


def ordenarPorPrecoDescendente(request):
    produtos = Produto.objects.order_by('-preco').filter(publicada=True)

    return render(request, 'mundoarte/index.html', {'produtos': produtos, 'categorias': categorias, 'subcategorias': subcategorias})


def filtrarPorCategoria(request):
    produtos = Produto.objects.filter(publicada=True)
    subcategorias = Subcategoria.objects.all()

    if 'filtroCategoria' in request.GET:
        categoria_buscada = request.GET['filtroCategoria']
        if categoria_buscada and categoria_buscada is not '0':

            categoria_selecionada = Categoria.objects.get(id=categoria_buscada)
            subcategorias = categoria_selecionada.subcategoria_set.all()

            produtos = produtos.filter(subcategoria__id__in=subcategorias)

    return render(request, 'mundoarte/index.html', {'produtos': produtos, 'categorias': categorias, 'subcategorias': subcategorias})


def filtrarPorSubcategoria(request):
    produtos = Produto.objects.filter(publicada=True)

    if 'filtroSubcategoria' in request.GET:
        categoria_buscada = request.GET['filtroSubcategoria']
        if categoria_buscada:
            produtos = produtos.filter(subcategoria=categoria_buscada)

    return render(request, 'mundoarte/index.html', {'produtos': produtos, 'categorias': categorias, 'subcategorias': subcategorias})


def sobre(request):
    return render(request, 'mundoarte/info/sobre.html')


def endereco(request):
    return render(request, 'mundoarte/info/endereco.html')


def redesSociais(request):
    return render(request, 'mundoarte/info/redes-sociais.html')