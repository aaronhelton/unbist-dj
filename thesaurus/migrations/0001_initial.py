# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('semantic', '0002_auto_20150827_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlternateLabel',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('semantic.property',),
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('semantic.resource',),
        ),
        migrations.CreateModel(
            name='Concept',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('semantic.resource',),
        ),
        migrations.CreateModel(
            name='ConceptScheme',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('semantic.resource',),
        ),
        migrations.CreateModel(
            name='PreferredLabel',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('semantic.property',),
        ),
        migrations.CreateModel(
            name='ScopeNote',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('semantic.property',),
        ),
    ]
