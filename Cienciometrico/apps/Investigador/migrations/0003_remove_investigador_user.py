# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-13 17:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Investigador', '0002_auto_20171208_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investigador',
            name='user',
        ),
    ]