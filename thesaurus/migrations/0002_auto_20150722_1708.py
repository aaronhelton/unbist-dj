# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesaurus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('match_type', models.CharField(max_length=200, choices=[(b'skos:broadMatch', b'has broad match'), (b'skos:relatedMatch', b'has related match'), (b'skos:narrowMatch', b'has narrow match'), (b'skos:closeMatch', b'has close match'), (b'skos:exactMatch', b'has exact match')])),
                ('match_target', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='resource_type',
            field=models.CharField(default=0, max_length=200, choices=[(b'skos:ConceptScheme', b'Concept Scheme'), (b'skos:Concept', b'Concept'), (b'skos:Collection', b'Collection'), (b'skos:OrderedCollection', b'Ordered Collection')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='property_type',
            field=models.CharField(max_length=200, choices=[(b'skos:prefLabel', b'has preferred label'), (b'skos:altLabel', b'has alternate label (UF)'), (b'skos:hiddenLabel', b'has hidden label'), (b'skos:notation', b'has notation'), (b'skos:note', b'has note'), (b'skos:changeNote', b'has change note'), (b'skos:definition', b'has definition'), (b'skos:editorialNote', b'has editorial note'), (b'skos:example', b'has example'), (b'skos:historyNote', b'has history note'), (b'skos:scopeNote', b'has scope note')]),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='relationship_target',
            field=models.ForeignKey(verbose_name=b'Target Resource', to='thesaurus.Resource'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='relationship_type',
            field=models.CharField(max_length=200, choices=[(b'skos:inScheme', b'is included in Concept Scheme'), (b'skos:hasTopConcept', b'has top Concept'), (b'skos:topConceptOf', b'is a top Concept of'), (b'skos:member', b'has member Concept'), (b'skos:broader', b'has broader Concept'), (b'skos:related', b'has related Concept'), (b'skos:narrower', b'has narrower Concept')]),
        ),
        migrations.AlterField(
            model_name='resource',
            name='datatype_properties',
            field=models.ManyToManyField(to='thesaurus.Property', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='object_properties',
            field=models.ManyToManyField(to='thesaurus.Relationship', null=True, blank=True),
        ),
    ]
