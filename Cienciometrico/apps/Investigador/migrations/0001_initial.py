# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-19 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carrera', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='investigador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cedula', models.CharField(blank=True, max_length=10)),
                ('Direccion', models.CharField(blank=True, max_length=500)),
                ('Coordenadas', models.CharField(blank=True, max_length=450)),
                ('Telefono', models.CharField(blank=True, max_length=10)),
                ('Genero', models.CharField(blank=True, max_length=100)),
                ('Ciudadania', models.CharField(blank=True, max_length=100)),
                ('carrera', models.ManyToManyField(to='carrera.carrera')),
            ],
        ),
    ]
