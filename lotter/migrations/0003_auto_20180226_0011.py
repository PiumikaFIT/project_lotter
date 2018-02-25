# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-25 18:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lotter', '0002_auto_20180225_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='assignee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
