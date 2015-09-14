# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('semantic', '0002_auto_20150827_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='label_class',
            field=models.ForeignKey(related_name='label_class', default=4, to='semantic.OwlSuper'),
        ),
    ]
