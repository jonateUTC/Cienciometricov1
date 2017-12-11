# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Investigador', '0002_auto_20171208_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=255)),
                ('Palabras_Clave', models.TextField()),
                ('Documentos', models.FileField(upload_to='eventos/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('Tipo_Proyecto', models.CharField(max_length=255)),
                ('investigador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Investigador.investigador')),
            ],
        ),
    ]