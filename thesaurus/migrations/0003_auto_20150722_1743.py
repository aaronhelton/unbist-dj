# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesaurus', '0002_auto_20150722_1708'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name_plural': 'properties'},
        ),
        migrations.RemoveField(
            model_name='resource',
            name='datatype_properties',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='object_properties',
        ),
        migrations.AddField(
            model_name='match',
            name='match_source',
            field=models.ForeignKey(default=0, to='thesaurus.Resource'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='source',
            field=models.ForeignKey(default=0, to='thesaurus.Resource'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='relationship',
            name='relationship_source',
            field=models.ForeignKey(default=0, to='thesaurus.Resource'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='relationship',
            name='relationship_target',
            field=models.ForeignKey(related_name='target_of', verbose_name=b'Target Resource', to='thesaurus.Resource'),
        ),
    ]
