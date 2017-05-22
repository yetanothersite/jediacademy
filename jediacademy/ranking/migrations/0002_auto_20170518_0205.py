# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 02:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rank',
            options={'verbose_name': 'rank', 'verbose_name_plural': 'ranks'},
        ),
        migrations.AlterModelOptions(
            name='rankregister',
            options={'verbose_name': 'rank register', 'verbose_name_plural': 'rank registers'},
        ),
        migrations.AlterField(
            model_name='rank',
            name='prev',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ranking.Rank'),
        ),
    ]