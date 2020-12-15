from django.contrib import admin
# Importar modelos
from .models import Page

# Configuración extra para el modelo Page
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    search_fields = ('titulo', 'contenido')
    list_filter = ('visible',)
    list_display = ('titulo', 'visible', 'fecha_creacion')

# Register your models here.
admin.site.register(Page, PageAdmin)

# Configuración del panel de administración
titulo = 'Proyecto Django - Daniel Pompa Pareja'
subtitulo = 'Panel de administración'

admin.site.site_header = titulo
admin.site.site_title = titulo
admin.site.index_title = subtitulo
