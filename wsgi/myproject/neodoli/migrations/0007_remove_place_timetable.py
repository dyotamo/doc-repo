# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neodoli', '0006_auto_20161123_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='timetable',
        ),
    ]
