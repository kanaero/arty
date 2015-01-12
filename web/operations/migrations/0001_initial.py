# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30, blank=True)),
                ('phone', models.CharField(max_length=15, blank=True)),
                ('fax', models.CharField(max_length=30, blank=True)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('address', models.TextField(blank=True)),
                ('contacts', models.ManyToManyField(to='operations.Contact', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30, blank=True)),
                ('phone', models.CharField(max_length=15, blank=True)),
                ('fax', models.CharField(max_length=30, blank=True)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('license_plate', models.CharField(max_length=10)),
                ('in_garage', models.BooleanField(default=False)),
                ('assigned_customer', models.ForeignKey(to='operations.Customer', blank=True)),
                ('assigned_driver', models.ForeignKey(to='operations.Driver', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='driver',
            name='assigned_truck',
            field=models.ForeignKey(to='operations.Truck', blank=True),
            preserve_default=True,
        ),
    ]
