# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0002_auto_20150110_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='assigned_truck',
        ),
    ]
