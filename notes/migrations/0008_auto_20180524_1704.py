# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-24 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_notes_hhh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='comment',
            field=models.CharField(blank=True, default='', max_length=100000, null=True),
        ),
    ]