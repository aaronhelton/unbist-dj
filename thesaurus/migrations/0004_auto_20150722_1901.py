# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesaurus', '0003_auto_20150722_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concept',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('thesaurus.resource',),
        ),
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name_plural': 'matches'},
        ),
    ]
