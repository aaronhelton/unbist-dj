# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('property_text', models.CharField(max_length=200)),
                ('property_language', models.CharField(max_length=2)),
                ('property_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relationship_type', models.CharField(max_length=200)),
                ('relationship_target', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uri', models.CharField(max_length=200)),
                ('datatype_properties', models.ManyToManyField(to='thesaurus.Property')),
                ('object_properties', models.ManyToManyField(to='thesaurus.Relationship')),
            ],
        ),
    ]
