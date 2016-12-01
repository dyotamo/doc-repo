# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neodoli', '0003_auto_20161121_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('city', models.CharField(choices=[('mpt', 'Maputo'), ('mtl', 'Matola'), ('xai', 'Xai-Xai'), ('ibn', 'Inhambane'), ('btw', 'Beira'), ('chm', 'Chimoio'), ('tet', 'Tete'), ('qlm', 'Quelimane'), ('npl', 'Nampula'), ('lcg', 'Lichinga'), ('pmb', 'Pemba')], max_length=35)),
                ('address', models.CharField(max_length=100)),
                ('tel1', models.CharField(verbose_name='Telephone 1', max_length=20)),
                ('tel2', models.CharField(blank=True, verbose_name='Telephone 2', null=True, max_length=20)),
                ('fax', models.CharField(blank=True, null=True, max_length=20)),
                ('email', models.EmailField(blank=True, null=True, max_length=50)),
                ('lat', models.FloatField(blank=True, verbose_name='Latitude', null=True)),
                ('lng', models.FloatField(blank=True, verbose_name='Longitude', null=True)),
                ('timetable', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('ph', 'Farmácia'), ('cli', 'Clínica'), ('lab', 'Laboratório')], max_length=3)),
            ],
        ),
        migrations.DeleteModel(
            name='Pharmacy',
        ),
    ]
