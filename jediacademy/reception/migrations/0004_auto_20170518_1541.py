# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 15:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0003_auto_20170518_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='planet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reception.Planet'),
        ),
    ]