# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-04 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Iso', models.CharField(max_length=2)),
                ('Nombre', models.CharField(max_length=150)),
            ],
        ),
    ]
