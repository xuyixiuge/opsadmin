# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_remove_systemuser_updatetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemuser',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='systemuser',
            name='user_role',
            field=models.CharField(choices=[('Admin', 'Administrator'), ('User', 'CommonUser')], default='User', max_length=10),
        ),
    ]
