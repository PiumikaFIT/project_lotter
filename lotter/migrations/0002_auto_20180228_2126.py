# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalleader',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='leader',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]