# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-28 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20160415_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='read_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
