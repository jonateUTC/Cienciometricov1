# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-03 17:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Investigador', '0003_remove_investigador_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='revista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=500)),
                ('Archivo', models.FileField(upload_to='revista/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('ISSN', models.CharField(max_length=250)),
                ('Base_Indexada', models.CharField(max_length=500)),
                ('Cuartil_Pertenece', models.CharField(max_length=500)),
                ('Factor_Impacto', models.CharField(max_length=500)),
                ('Url', models.URLField()),
                ('investigador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Investigador.investigador')),
            ],
        ),
    ]
