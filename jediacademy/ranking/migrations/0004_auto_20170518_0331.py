# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0003_auto_20170518_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rank',
            name='name',
            field=models.CharField(max_length=12, verbose_name='name'),
        ),
    ]
