# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neodoli', '0007_remove_place_timetable'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='is_24',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
