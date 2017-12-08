# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-08 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='investigacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=255)),
                ('Palabras_Claves', models.TextField()),
                ('Resumen', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('Fecha', models.DateField()),
                ('Editor', models.CharField(max_length=255)),
                ('Url', models.URLField()),
            ],
        ),
    ]
