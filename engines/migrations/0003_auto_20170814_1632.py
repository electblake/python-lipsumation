# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engines', '0002_engine_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engine',
            name='slug',
            field=models.CharField(max_length=200, verbose_name='engine slug'),
        ),
    ]