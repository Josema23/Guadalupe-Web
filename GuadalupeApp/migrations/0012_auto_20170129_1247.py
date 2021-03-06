# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-29 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuadalupeApp', '0011_auto_20170129_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='culto',
        ),
        migrations.AddField(
            model_name='album',
            name='titulo',
            field=models.CharField(choices=[(b'Viajes', b'Viajes'), (b'Encuentros', b'Encuentros'), (b'Novena', b'Novena'), (b'Serenata', b'Serenata'), (b'Verbena', b'Verbena'), (b'Presentacion', b'Presentacion a la Virgen')], default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='portada',
            field=models.ImageField(upload_to=b''),
        ),
    ]
