# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-19 08:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20180819_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='permission',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='permissions.Permission'),
        ),
    ]
