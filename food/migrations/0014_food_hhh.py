# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-15 00:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0013_auto_20170909_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='hhh',
            field=models.CharField(default='1018', max_length=4),
        ),
    ]
