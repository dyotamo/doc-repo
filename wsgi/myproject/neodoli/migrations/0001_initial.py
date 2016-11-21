# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=35)),
                ('city', models.CharField(max_length=35, choices=[('mpt', 'Maputo'), ('mtl', 'Matola'), ('xai', 'Xai-Xai'), ('ibn', 'Inhambane'), ('btw', 'Beira'), ('chm', 'Chimoio'), ('tet', 'Tete'), ('qlm', 'Quelimane'), ('npl', 'Nampula'), ('lcg', 'Lichinga'), ('pmb', 'Pemba')])),
                ('address', models.CharField(max_length=100)),
                ('tel1', models.CharField(verbose_name='Telephone 1', max_length=20)),
                ('tel2', models.CharField(null=True, verbose_name='Telephone 2', max_length=20, blank=True)),
                ('fax', models.CharField(null=True, max_length=20, blank=True)),
                ('email', models.EmailField(null=True, max_length=50, blank=True)),
                ('lat', models.FloatField(null=True, verbose_name='Latitude', blank=True)),
                ('lng', models.FloatField(null=True, verbose_name='Longitude', blank=True)),
                ('timetable', models.CharField(max_length=50)),
            ],
        ),
    ]
