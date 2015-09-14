# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('semantic', '0005_auto_20150828_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='match_internal_model',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='match',
            name='match_internal_uri',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='match',
            name='match_internal_view',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='match_target',
            field=models.URLField(null=True, blank=True),
        ),
    ]
