# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-21 06:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_auto_20171129_0234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AssetEnable', models.BooleanField(default=False)),
                ('PermEnable', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='admin_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permission',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Permission'),
        ),
    ]