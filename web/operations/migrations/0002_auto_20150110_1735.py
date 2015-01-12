# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='assigned_truck',
            field=models.ForeignKey(blank=True, to='operations.Truck', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='truck',
            name='assigned_customer',
            field=models.ForeignKey(blank=True, to='operations.Customer', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='truck',
            name='assigned_driver',
            field=models.ForeignKey(blank=True, to='operations.Driver', null=True),
            preserve_default=True,
        ),
    ]
