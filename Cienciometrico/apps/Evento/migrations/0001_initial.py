# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-10 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=250, null=True)),
                ('Lugar', models.CharField(max_length=250, null=True)),
                ('Fecha', models.DateField(null=True)),
            ],
        ),
    ]