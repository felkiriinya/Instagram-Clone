# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-22 18:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0010_auto_20201122_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='user',
        ),
    ]
