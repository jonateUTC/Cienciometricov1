# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-08 16:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Formacion_Academica', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formacion_academica',
            options={'permissions': (('ver_formacionAcademica', 'ver formacionAcademica'),)},
        ),
    ]