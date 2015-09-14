# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('semantic', '0003_auto_20150828_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='label_class',
            field=models.ForeignKey(related_name='label_class', to='semantic.OwlSuper'),
        ),
    ]
