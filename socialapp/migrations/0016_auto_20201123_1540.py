# Generated by Django 3.1.3 on 2020-11-23 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0015_auto_20201123_1528'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='image',
            new_name='post',
        ),
    ]