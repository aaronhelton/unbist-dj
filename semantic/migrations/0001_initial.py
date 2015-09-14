# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('match_target', models.URLField()),
                ('resolve_label', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='OwlSuper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owl_type', models.CharField(max_length=200, choices=[(b'owl:Class', b'Class'), (b'owl:DatatypeProperty', b'DatatypeProperty'), (b'owl:ObjectProperty', b'ObjectProperty')])),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Prefix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('uri', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'prefixes',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('property_text', models.TextField()),
                ('property_language', models.CharField(max_length=2, choices=[(b'ar', 'Arabic'), (b'zh', 'Chinese'), (b'en', 'English'), (b'fr', 'French'), (b'ru', 'Russian'), (b'es', 'Spanish')])),
            ],
            options={
                'ordering': ['property_type', 'property_language', 'property_text'],
                'verbose_name_plural': 'properties',
            },
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uri', models.CharField(max_length=200)),
                ('label_class', models.ForeignKey(related_name='label_class', to='semantic.OwlSuper')),
                ('resource_type', models.ForeignKey(to='semantic.OwlSuper')),
            ],
        ),
        migrations.AddField(
            model_name='relationship',
            name='relationship_source',
            field=models.ForeignKey(to='semantic.Resource'),
        ),
        migrations.AddField(
            model_name='relationship',
            name='relationship_target',
            field=models.ForeignKey(related_name='target_of', verbose_name=b'Target Resource', to='semantic.Resource'),
        ),
        migrations.AddField(
            model_name='relationship',
            name='relationship_type',
            field=models.ForeignKey(to='semantic.OwlSuper'),
        ),
        migrations.AddField(
            model_name='property',
            name='property_source',
            field=models.ForeignKey(to='semantic.Resource'),
        ),
        migrations.AddField(
            model_name='property',
            name='property_type',
            field=models.ForeignKey(to='semantic.OwlSuper'),
        ),
        migrations.AddField(
            model_name='owlsuper',
            name='prefix',
            field=models.ForeignKey(to='semantic.Prefix'),
        ),
        migrations.AddField(
            model_name='match',
            name='match_source',
            field=models.ForeignKey(to='semantic.Resource'),
        ),
        migrations.AddField(
            model_name='match',
            name='match_type',
            field=models.ForeignKey(to='semantic.OwlSuper'),
        ),
    ]
