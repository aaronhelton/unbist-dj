# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesaurus', '0004_auto_20150722_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('thesaurus.property',),
        ),
    ]
