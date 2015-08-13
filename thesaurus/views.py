#from django.http import Http404
from django.shortcuts import get_object_or_404, render

# Create your views here.
#from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template.context_processors import i18n
from django.utils import translation

from .models import ConceptScheme
from .models import Resource



def index(request):
    concept_schemes = ConceptScheme.objects.get(uri='00')
    template = loader.get_template('thesaurus/index.html')
    context = RequestContext(request, {
        'concept_schemes': concept_schemes,
    })
    return render(request, 'thesaurus/index.html', context)
    
def resource(request, uri):
    resource = get_object_or_404(Resource, uri=uri)
    microthesauri = Resource.objects.filter(relationship__relationship_target = resource, relationship__relationship_type = 'skos:member')
    return render(request, 'thesaurus/detail.html', {'resource': resource, 'microthesauri': microthesauri})
    
def scheme(request, uri):
    resource = get_object_or_404(Resource, uri=uri)
    collections = Resource.objects.filter(relationship__relationship_target = resource, relationship__relationship_type = 'skos:inScheme', resource_type = 'skos:Collection')
    return render(request, 'thesaurus/scheme.html', {'resource': resource, 'collections': collections})