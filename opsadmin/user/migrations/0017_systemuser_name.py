# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 03:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_auto_20171120_0735'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemuser',
            name='name',
            field=models.CharField(max_length=50, null=True, unique=True, verbose_name='Name'),
        ),
    ]