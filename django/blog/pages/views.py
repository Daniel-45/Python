from django.shortcuts import render
#  Importar modelos
from .models import Page
# Importar decoradores 
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def page(request, slug):

    """
    Acceder al modelo Page, a los objetos de la base de datos y sacar uno
    con la condición de que el slug sea igual al slug que llega por la URL
    Es el equivalente a SQL:
    'SELECT * FROM pages WHERE slug = %s
    """
    page = Page.objects.get(slug=slug)

    return render(request, 'pages/page.html', {
        'page': page
    })