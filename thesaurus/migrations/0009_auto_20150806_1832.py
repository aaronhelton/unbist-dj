# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesaurus', '0008_auto_20150806_1503'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='source',
            new_name='property_source',
        ),
    ]
