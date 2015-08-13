# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesaurus', '0007_auto_20150722_2020'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'ordering': ['property_type', 'property_language', 'property_text'], 'verbose_name_plural': 'properties'},
        ),
    ]
