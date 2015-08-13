# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesaurus', '0005_label'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Label',
        ),
        migrations.CreateModel(
            name='AltLabel',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('thesaurus.property',),
        ),
        migrations.CreateModel(
            name='PrefLabel',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('thesaurus.property',),
        ),
    ]
