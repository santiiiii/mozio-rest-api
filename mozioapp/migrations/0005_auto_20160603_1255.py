# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mozioapp', '0004_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='lat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='point',
            name='lon',
            field=models.FloatField(),
        ),
    ]
