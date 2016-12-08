# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neodoli', '0008_place_is_24'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='is_24',
            field=models.BooleanField(verbose_name='Is 24 hour?'),
        ),
    ]
