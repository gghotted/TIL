from django.conf import settings


def url_params(request):
    return {'url_params': request.resolver_match.kwargs}


def categories(request):
    return {'categories': settings.CATEGORIES}