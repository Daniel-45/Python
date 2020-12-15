from django.db import models
""" 
Para instalar CKEditor usar el comando:
- pip install django-ckeditor
Importar RichTextField
Hay que cargar la app de CKEditor en settings
"""
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    titulo = models.CharField(max_length=50, verbose_name='Título')
    contenido = RichTextField(verbose_name='Contenido')
    slug = models.CharField(unique=True, max_length=200, verbose_name='URL amigable')
    visible = models.BooleanField(verbose_name='Visible')
    posicion = models.IntegerField(default=0, verbose_name='Posicion')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Actualizado')

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'

    def __str__(self):
        return self.titulo
    