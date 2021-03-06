# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-18 20:23
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('time_stamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, primary_key=True, serialize=False)),
                ('customer_name', models.TextField()),
                ('emails', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=64), size=None)),
                ('phone_numbers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), blank=True, size=None)),
                ('status', models.CharField(choices=[(b'hot', b'Hot'), (b'warm', b'Warm'), (b'Cold', b'cold')], max_length=5, null=True)),
                ('appointment', models.DateTimeField(null=True)),
                ('assigned_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_assigned_to', to=settings.AUTH_USER_MODEL)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_assigned_by', to=settings.AUTH_USER_MODEL)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leads.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, primary_key=True, serialize=False)),
                ('transaction_id', models.TextField()),
                ('transaction_type', models.TextField()),
                ('details', django.contrib.postgres.fields.jsonb.JSONField(verbose_name=b'transaction_details')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deal_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('source', models.TextField()),
                ('company_name', models.TextField()),
                ('emails', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=64), size=None)),
                ('phone_numbers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), size=None)),
                ('status', models.CharField(choices=[(b'hot', b'Hot'), (b'warm', b'Warm'), (b'Cold', b'cold')], max_length=5, null=True)),
                ('appointment', models.DateTimeField(null=True)),
                ('assigned_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lead_assigned_to', to=settings.AUTH_USER_MODEL)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lead_assigned_by', to=settings.AUTH_USER_MODEL)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leads.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Reminders',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('time_stamp', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddIndex(
            model_name='lead',
            index=models.Index(fields=[b'company_name', b'emails', b'assigned_by', b'assigned_to', b'phone_numbers'], name='leads_lead_company_4d123c_idx'),
        ),
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=[b'customer_name', b'emails', b'assigned_by', b'assigned_to', b'phone_numbers'], name='leads_custo_custome_193f0a_idx'),
        ),
    ]
