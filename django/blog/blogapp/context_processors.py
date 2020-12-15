from blogapp.models import Categoria, Articulo

def get_categories(request):

    # Id's de los artículos
    ids = Articulo.objects.filter(publico=True).values_list('categorias', flat=True)
    # Subconsulta
    categorias = Categoria.objects.filter(id__in=ids).values_list('id', 'nombre')
    return {
        'categorias': categorias,
        'ids': ids
    }