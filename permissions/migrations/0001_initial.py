# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-18 20:23
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, primary_key=True, serialize=False)),
                ('leads', models.BooleanField(default=False)),
                ('deals', models.BooleanField(default=False)),
                ('customers', models.BooleanField(default=False)),
                ('users', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'permissions_permission',
            },
        ),
    ]
