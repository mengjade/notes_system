# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-15 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_notes_info_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='hhh',
            field=models.CharField(default='1018', max_length=4),
        ),
    ]