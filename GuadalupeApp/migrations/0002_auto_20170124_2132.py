# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-24 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuadalupeApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='junta',
            name='miembro',
        ),
        migrations.AddField(
            model_name='junta',
            name='miembro',
            field=models.ManyToManyField(to='GuadalupeApp.Miembros'),
        ),
    ]
