# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-22 06:41
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('L_F_app', '0003_auto_20171222_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=1000, null=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]