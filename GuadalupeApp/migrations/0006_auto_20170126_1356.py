# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-26 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuadalupeApp', '0005_auto_20170125_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='cultos',
            name='imagen2',
            field=models.ImageField(default=0, upload_to=b''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cultos',
            name='desarrollo',
            field=models.TextField(max_length=500),
        ),
    ]
