# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 03:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olahfisik', '0002_auto_20171120_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='busy',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='close',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='open',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
