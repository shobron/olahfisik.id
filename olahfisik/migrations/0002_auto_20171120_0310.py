# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 03:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olahfisik', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='rating',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='address',
            field=models.CharField(max_length=265, null=True),
        ),
    ]