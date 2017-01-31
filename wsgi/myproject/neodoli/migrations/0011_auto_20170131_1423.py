# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neodoli', '0010_remove_place_is_24'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='e1',
            field=models.PositiveIntegerField(verbose_name='Primeira entrada', default=8),
        ),
        migrations.AddField(
            model_name='place',
            name='e2',
            field=models.PositiveIntegerField(verbose_name='Segunda entrada', default=14),
        ),
        migrations.AddField(
            model_name='place',
            name='s1',
            field=models.PositiveIntegerField(verbose_name='Primeira saída', default=12),
        ),
        migrations.AddField(
            model_name='place',
            name='s2',
            field=models.PositiveIntegerField(verbose_name='Segunda saída', default=18),
        ),
    ]
