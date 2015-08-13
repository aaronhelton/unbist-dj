# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesaurus', '0006_auto_20150722_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('thesaurus.resource',),
        ),
        migrations.CreateModel(
            name='ConceptScheme',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('thesaurus.resource',),
        ),
        migrations.AlterModelOptions(
            name='altlabel',
            options={'verbose_name': 'Alternate Label', 'verbose_name_plural': 'Alternate Labels'},
        ),
        migrations.AlterModelOptions(
            name='preflabel',
            options={'verbose_name': 'Preferred Label', 'verbose_name_plural': 'Preferred Labels'},
        ),
    ]
