# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neodoli', '0002_auto_20161121_1112'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pharmacy',
            options={'verbose_name_plural': 'Pharmacies'},
        ),
    ]
