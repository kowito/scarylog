from django.conf import settings

def template_global_params(request):
    return {
        'ALGOLIA_APPLICATION_ID': settings.ALGOLIA.get('APPLICATION_ID'),
        'ALGOLIA_API_KEY': settings.ALGOLIA.get('API_KEY'),
    }
