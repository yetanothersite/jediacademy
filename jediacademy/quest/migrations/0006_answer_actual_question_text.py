# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0005_auto_20170518_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='actual_question_text',
            field=models.TextField(default='Lorem Ipsum', verbose_name='actual question text'),
            preserve_default=False,
        ),
    ]
