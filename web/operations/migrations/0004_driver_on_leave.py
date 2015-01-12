# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0003_remove_driver_assigned_truck'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='on_leave',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
