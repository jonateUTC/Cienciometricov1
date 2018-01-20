# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-19 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=255)),
                ('Resumen', models.TextField()),
                ('Palabras_Claves', models.TextField()),
                ('Tipo', models.CharField(max_length=255)),
                ('LineaInvestigacion', models.CharField(max_length=255)),
                ('Documentos', models.FileField(null=True, upload_to='proyecto/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'permissions': (('ver_Proyectos', 'ver Proyectos'),),
            },
        ),
    ]
