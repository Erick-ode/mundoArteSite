from django.contrib import admin
from mundoarte.models import Categoria, Subcategoria, Produto


class ListaCategorias(admin.ModelAdmin):
    list_display = ('id', 'nome',)
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_per_page = 10


class ListaSubcategorias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria',)
    list_display_links = ('nome',)
    search_fields = ('nome', 'categoria__nome')
    list_filter = ('categoria',)
    list_editable = ('categoria',)
    list_per_page = 10


class ListaProdutos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'preco', 'subcategoria', 'publicada')
    list_display_links = ('nome',)
    search_fields = ('nome', 'categoria', 'subcategoria',)
    list_filter = ('subcategoria', 'categoria',)
    list_editable = ('subcategoria', 'publicada', 'categoria')
    list_per_page = 10


admin.site.register(Categoria, ListaCategorias)
admin.site.register(Subcategoria, ListaSubcategorias)
admin.site.register(Produto, ListaProdutos)




