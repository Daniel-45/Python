from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
# Importar modelos
from blogapp.models import Categoria, Articulo
# Importar decoradores 
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def articulos(request):

    # Sacar todos los objetos de la base de datos
    articulos = Articulo.objects.all()

    # Paginación de los artículos
    paginator = Paginator(articulos, 2)

    # Recoger número de página
    pagina = request.GET.get('page')
    pagina_articulos = paginator.get_page(pagina)

    return render(request, 'articulos/articulos.html',  {
        'titulo': 'Artículos',
        'articulos': pagina_articulos
    })

@login_required(login_url='login')
def categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    # categoria = Categoria.objects.get(id=categoria_id)

    articulos = Articulo.objects.filter(categorias=categoria_id)

    return render(request, 'categorias/categoria.html', {
        'categoria': categoria,
        'articulos': articulos
    })

@login_required(login_url='login')
def articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, id=articulo_id)

    return render(request, 'articulos/articulo.html', {
        'articulo': articulo
    })
