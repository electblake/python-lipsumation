# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engines', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='engine',
            name='slug',
            field=models.CharField(default='', max_length=200, verbose_name='engine slug'),
        ),
    ]
