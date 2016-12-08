# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neodoli', '0009_auto_20161204_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='is_24',
        ),
    ]
