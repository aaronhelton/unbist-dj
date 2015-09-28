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
from django.conf import settings

from .models import Resource
from .models import OwlSuper
from .models import Prefix

def index(request):
    apps = settings.ROUTABLE_APPS
    return render(request, 'semantic/index.html', {'apps': apps})

def resource(request, uri):
    resource = get_object_or_404(Resource, uri=uri)
    prefixes = Prefix.objects.all
    return render(request, 'semantic/detail.html', {'resource': resource, 'prefixes': prefixes })    

def autocomplete(request):
    #sqs = SearchQuerySet().autocomplete(text_auto=request.GET.get('q', ''))[:10]
    sqs_labels = SearchQuerySet().autocomplete(labels=request.GET.get('q', ''))
    sqs_notes = SearchQuerySet().autocomplete(notes=request.GET.get('q', ''))
    sqs_rels = SearchQuerySet().autocomplete(relationships=request.GET.get('q', ''))
    sqs = sqs_labels | sqs_notes | sqs_rels
    suggestions = []
    for result in sqs[:10]:
        res_id = result.id.split('.')[2]
        res = Resource.objects.get(id=res_id)
        suggestions.append({'value': res.pref_label(), 'url': res.uri})
    # Make sure you return a JSON object, not a bare list.
    # Otherwise, you could be vulnerable to an XSS attack.
    the_data = json.dumps(
        suggestions
    )
    return HttpResponse(the_data, content_type='application/json')
