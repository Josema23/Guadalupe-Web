# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-29 11:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GuadalupeApp', '0009_auto_20170126_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('culto', models.CharField(choices=[(b'Novena', b'Novena'), (b'Serenata', b'Serenata'), (b'Verbena', b'Verbena'), (b'Presentacion', b'Presentacion a la Virgen')], max_length=50)),
                ('owner', models.CharField(max_length=60)),
                ('portada', models.ImageField(upload_to=b'Guadalupe/media/Galeria/')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AlbumImagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to=b'Guadalupe/media/Galeria/')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='GuadalupeApp.Album')),
            ],
        ),
        migrations.AlterField(
            model_name='noticia',
            name='intro',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
