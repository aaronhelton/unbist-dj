from django.shortcuts import render
import json
from django.http import HttpResponse
from haystack.query import SearchQuerySet
from django.core.urlresolvers import resolve

# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader
from django.template.context_processors import i18n
from django.utils import translation

from .models import Resource
from .models import OwlSuper
from .models import Prefix

def index(request):
    apps = ('thesaurus','votedb')
    return render(request, 'semantic/index.html', {'apps': apps})

def resource(request, uri):
    resource = get_object_or_404(Resource, uri=uri)
    prefixes = Prefix.objects.all
    return render(request, 'semantic/detail.html', {'resource': resource, 'prefixes': prefixes })    

def autocomplete(request):
    sqs = SearchQuerySet().autocomplete(text_auto=request.GET.get('q', ''))[:5]
    suggestions = []
    for result in sqs:
        res_id = result.id.split('.')[2]
        res = Resource.objects.get(id=res_id)
        suggestions.append({'value': res.pref_label(), 'url': res.uri, 'request':'request.current_app'})
    # Make sure you return a JSON object, not a bare list.
    # Otherwise, you could be vulnerable to an XSS attack.
    the_data = json.dumps(
        suggestions
    )
    return HttpResponse(the_data, content_type='application/json')
