from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader
from django.template.context_processors import i18n
from django.utils import translation
#from haystack.utils import Highlighter

from .models import Concept
from .models import Collection
from .models import Resource
from .models import OwlSuper
from .models import ConceptScheme

def index(request):
    concept_schemes = ConceptScheme.objects.all
    return render(request, 'thesaurus/index.html', {'concept_schemes': concept_schemes})

def resource(request, uri):
    resource = get_object_or_404(Resource, uri=uri)
    microthesauri = Resource.objects.filter(relationship__relationship_target = resource, relationship__relationship_type = OwlSuper.objects.get(name='member').id)
    return render(request, 'thesaurus/detail.html', {'resource': resource, 'microthesauri': microthesauri, 'uri': uri })

def scheme(request, uri):
    concept_scheme = get_object_or_404(ConceptScheme, uri=uri)
    domains = Collection.objects.filter(uri__regex = r'^\d\d$')
    return render(request, 'thesaurus/scheme.html', {'concept_scheme': concept_scheme, 'domains': domains, 'uri': uri})

def collection(request, uri):
    collection = get_object_or_404(Collection, uri=uri)
    children = collection.relationship_set.filter(relationship_type = OwlSuper.objects.get(name='member').id)
    return render(request, 'thesaurus/collection.html', {'collection': collection, 'children': children, 'uri': uri})

