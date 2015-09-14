# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def find_internal_matches(apps, schema_editor):
    Property = apps.get_model('semantic','Property')
    Resource = apps.get_model('semantic','Resource')
    OwlSuper = apps.get_model('semantic','OwlSuper')
    Match = apps.get_model('semantic', 'Match')
    labels = Property.objects.filter(property_language='en', property_type=OwlSuper.objects.get(name='prefLabel'))
    #resources = Resource.objects.all()
 
    for label in labels:
        sane_label = label.property_text.replace(')','_').replace('(','_').replace(' ','_')
        potential = ''
        try:
            potential = Resource.objects.get(uri=sane_label)
        except Resource.DoesNotExist:
            pass
        else:
            match = Match.objects.create(
                match_source=label.property_source, 
                match_type=OwlSuper.objects.get(name='exactMatch'), 
                match_internal_model = 'votedb',
                match_internal_view = 'voter',
                match_internal_uri = sane_label,
                resolve_label = True
            )
            match.save()

class Migration(migrations.Migration):

    dependencies = [
        ('semantic', '0006_auto_20150911_1535'),
    ]

    operations = [
        migrations.RunPython(find_internal_matches),
    ]
