# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 08:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0002_auto_20170518_0801'),
        ('quest', '0002_auto_20170518_0801'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='exam',
            unique_together=set([('person', 'quest')]),
        ),
    ]
