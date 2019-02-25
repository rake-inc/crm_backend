# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-19 08:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0001_initial'),
        ('users', '0013_auto_20180819_0229'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='permission',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='permissions.Permission'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigIntegerField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=[b'username', b'email', b'phone_numbers'], name='users_user_usernam_118b29_idx'),
        ),
        migrations.AlterModelTable(
            name='user',
            table='users_user',
        ),
    ]