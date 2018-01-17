# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-20 04:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20171117_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.CharField(blank=True, choices=[('ops', 'Operation Engineer'), ('dev', 'Development Engineer')], max_length=30, null=True),
        ),
    ]