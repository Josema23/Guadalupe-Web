# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-04 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuadalupeApp', '0016_albumimagen_pie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiaas',
            name='historia',
            field=models.TextField(blank=True, max_length=1500),
        ),
        migrations.AlterField(
            model_name='historiaas',
            name='historia2',
            field=models.TextField(blank=True, max_length=1500),
        ),
        migrations.AlterField(
            model_name='historiaas',
            name='historia3',
            field=models.TextField(blank=True, max_length=1500),
        ),
    ]
