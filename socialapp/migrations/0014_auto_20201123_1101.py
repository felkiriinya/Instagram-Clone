# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-23 08:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0013_auto_20201123_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='socialapp.Profile'),
        ),
    ]