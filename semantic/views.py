from django.shortcuts import render

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
