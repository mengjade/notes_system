# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-06 02:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0009_delete_sweet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='unit',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]