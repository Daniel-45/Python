from django.db import models
from ckeditor.fields import RichTextField
# Importar modelo Usuario del panel de administración Django
from django.contrib.auth.models import User

# Create your models here.

# Categorías
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.CharField(max_length=255, verbose_name='Descripcion')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Creada')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre

# Artículos
class Articulo(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    contenido = RichTextField(verbose_name='Contenido')
    imagen  = models.ImageField(default='null', verbose_name='Imagen', upload_to='articulos')
    publico = models.BooleanField(verbose_name='Publicado')
    """ 
    Relación 1-1 con el modelo Usuario del panel de administración Django
    En la base de datos, dentro de la propiedad user va a guardar el
    id del usuario que ha creado el artículo.
    En la propiedad 'usuario' habrá un objeto completo del modelo Usuario
    """
    usuario = models.ForeignKey(User, editable=False, verbose_name='Usuario', on_delete=models.CASCADE)
    """ 
    Relación n-m con el modelo Categoria
    """
    categorias = models.ManyToManyField(Categoria,verbose_name='Categorías', blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Editado')

    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.titulo
    


