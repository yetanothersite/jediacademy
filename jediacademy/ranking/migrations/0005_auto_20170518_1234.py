# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0004_auto_20170518_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rank',
            name='name',
            field=models.CharField(max_length=12, unique=True, verbose_name='name'),
        ),
    ]
