from pages.models import Page

def get_pages(request):
    pages = Page.objects.filter(visible=True).order_by('posicion').values_list('id', 'titulo', 'slug')
    return {
        'pages': pages
    }