# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operations', '0005_historicallocation'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalContact',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30, blank=True)),
                ('phone', models.CharField(max_length=15, blank=True)),
                ('fax', models.CharField(max_length=30, blank=True)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('description', models.TextField(blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical contact',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalCustomer',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('name', models.CharField(max_length=80)),
                ('address', models.TextField(blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical customer',
            },
            bases=(models.Model,),
        ),
    ]
