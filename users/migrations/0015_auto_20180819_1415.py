# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-19 08:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20180819_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='permission',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='permissions.Permission'),
        ),
    ]
