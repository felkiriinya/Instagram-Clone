# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-22 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0005_auto_20201122_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]