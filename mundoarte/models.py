from django.db import models
from pathlib import os
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    

class Subcategoria(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome
    

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.SET_NULL)
    subcategoria = models.ForeignKey(Subcategoria, null=True, blank=True, on_delete=models.SET_NULL)
    preco = models.FloatField()
    imagem = models.ImageField(upload_to='fotos/%Y/%m/%d/', null=True, blank=True)
    data_publicacao = models.DateTimeField(default=datetime.now, blank=False)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
    
    def delete(self, *args, **kwargs):
        if self.imagem:
            if os.path.isfile(self.imagem.path):
                os.remove(self.imagem.path)
        super(Produto, self).delete(*args, **kwargs)


@receiver(pre_save, sender=Produto)
def atualizar_categoria(sender, instance, **kwargs):
    if instance.pk is None and instance.subcategoria and instance.subcategoria.categoria:
        instance.categoria = instance.subcategoria.categoria
