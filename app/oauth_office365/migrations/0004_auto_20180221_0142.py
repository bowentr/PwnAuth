# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-21 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth_office365', '0003_auto_20171025_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='victim',
            name='expires_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='victim',
            name='refresh_token',
            field=models.TextField(blank=True, null=True),
        ),
    ]
