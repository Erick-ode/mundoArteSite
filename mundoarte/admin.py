from django.contrib import admin
from mundoarte.models import Categoria, Subcategoria, Produto


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome',)
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_per_page = 10


class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria',)
    list_display_links = ('nome',)
    search_fields = ('nome', 'categoria__nome')
    list_filter = ('categoria',)
    list_editable = ('categoria',)
    list_per_page = 10


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'preco', 'subcategoria', 'publicada', 'data_publicacao')
    list_display_links = ('nome',)
    search_fields = ('nome', 'categoria__nome', 'subcategoria__nome')
    list_filter = ('subcategoria', 'subcategoria__categoria')
    list_editable = ('subcategoria', 'publicada',)
    list_per_page = 10


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Subcategoria, SubcategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)




