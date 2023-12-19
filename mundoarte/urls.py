from django.urls import path
from mundoarte.views import index, buscar, ordenarPorNome, ordenarPorPrecoCrescente, ordenarPorPrecoDescendente, sobre, endereco, redesSociais

urlpatterns = [
    path('', index, name='index'),
    path('buscar', buscar, name='buscar'),
    path('ordenar', ordenarPorNome, name='ordenarPorNome'),
    path('ordenar-crescente', ordenarPorPrecoCrescente, name='ordenarPorPrecoCrescente'),
    path('ordenar-descrescente', ordenarPorPrecoDescendente, name='ordenarPorPrecoDescendente'),
    path('sobre', sobre, name='sobre'),
    path('endereco', endereco, name='endereco'),
    path('redesSociais', redesSociais, name='redesSociais'),
]
