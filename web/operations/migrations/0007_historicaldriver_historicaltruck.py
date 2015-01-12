# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operations', '0006_historicalcontact_historicalcustomer'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalDriver',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30, blank=True)),
                ('phone', models.CharField(max_length=15, blank=True)),
                ('fax', models.CharField(max_length=30, blank=True)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('description', models.TextField(blank=True)),
                ('on_leave', models.BooleanField(default=False)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical driver',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalTruck',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('license_plate', models.CharField(max_length=10)),
                ('assigned_driver_id', models.IntegerField(db_index=True, null=True, blank=True)),
                ('assigned_customer_id', models.IntegerField(db_index=True, null=True, blank=True)),
                ('in_garage', models.BooleanField(default=False)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical truck',
            },
            bases=(models.Model,),
        ),
    ]
