# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def load_skos_ontology(apps, schema_editor):
    Prefix = apps.get_model('semantic','Prefix')
    prefix = Prefix.objects.create(name='skos', uri = 'http://www.w3.org/2004/02/skos/core')
    prefix.save()

    SKOS = (
        ('owl:Class','Concept'),
        ('owl:Class','ConceptScheme'),
        ('owl:Class','Collection'),
        ('owl:DatatypeProperty','prefLabel'),
        ('owl:DatatypeProperty','altLabel'),
        ('owl:DatatypeProperty','scopeNote'),
        ('owl:ObjectProperty','broader'),
        ('owl:ObjectProperty','narrower'),
        ('owl:ObjectProperty','related'),
        ('owl:ObjectProperty','exactMatch'),
        ('owl:ObjectProperty','closeMatch'),
        ('owl:ObjectProperty','narrowMatch'),
        ('owl:ObjectProperty','broadMatch'),
        ('owl:ObjectProperty','member'),
        ('owl:ObjectProperty','hasTopConcept'),
        ('owl:ObjectProperty','topConceptOf'),
        ('owl:ObjectProperty','inScheme'),
    )
    
    OwlSuper = apps.get_model('semantic','OwlSuper')

    for o_type, o_name in SKOS:
        oc = OwlSuper.objects.create(prefix=Prefix.objects.get(name='skos'),owl_type=o_type,name=o_name)
        oc.save()

class Migration(migrations.Migration):

    dependencies = [
        ('semantic', '0004_auto_20150828_1725'),
    ]

    operations = [
        migrations.RunPython(load_skos_ontology),
    ]
