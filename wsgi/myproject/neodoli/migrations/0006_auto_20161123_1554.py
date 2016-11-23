# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neodoli', '0005_place_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(blank=True, upload_to='%Y/%m/%d', null=True),
        ),
    ]
