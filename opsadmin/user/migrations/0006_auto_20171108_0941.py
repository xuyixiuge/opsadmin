# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 09:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_onlineuserstatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onlineuserstatus',
            name='user',
        ),
        migrations.DeleteModel(
            name='OnlineUserStatus',
        ),
    ]