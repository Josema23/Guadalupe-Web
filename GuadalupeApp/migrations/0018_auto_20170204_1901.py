# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-04 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuadalupeApp', '0017_auto_20170204_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiaas',
            name='historia',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='historiaas',
            name='historia2',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='historiaas',
            name='historia3',
            field=models.TextField(blank=True),
        ),
    ]
