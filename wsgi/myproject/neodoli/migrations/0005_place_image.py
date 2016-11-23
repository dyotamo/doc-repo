# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neodoli', '0004_auto_20161123_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='image',
            field=models.ImageField(null=True, upload_to='', blank=True),
        ),
    ]
