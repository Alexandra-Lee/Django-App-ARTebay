# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-20 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20180920_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='occupation',
            field=models.CharField(max_length=120, null=True),
        ),
    ]