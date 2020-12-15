from django.contrib import admin
# Importar modelos
from .models import Categoria, Articulo

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion',)
    list_display = ('nombre', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')

class ArticuloAdmin(admin.ModelAdmin):
    readonly_fields = ('usuario', 'fecha_creacion', 'fecha_actualizacion')
    list_display = ('titulo', 'usuario', 'publico', 'fecha_creacion')
    search_fields = ('titulo', 'contenido', 'usuario__username', 'categorias__nombre')
    list_filter = ('publico', 'usuario__username', 'categorias__nombre')

    def save_model(self, request, obj, form, change):
        """
        Si no llega un id de usuario guadar el id del usuario identificado 
        que llega en la solicitud
        """
        if not obj.usuario_id:
            obj.usuario_id = request.user.id

        obj.save()

# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Articulo, ArticuloAdmin)