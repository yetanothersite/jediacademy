# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 15:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0005_auto_20170518_1234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rankregister',
            old_name='master',
            new_name='mentor',
        ),
        migrations.AddField(
            model_name='rank',
            name='are_mentors',
            field=models.BooleanField(default=True, verbose_name='are mentors?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rank',
            name='prev',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='ranking.Rank'),
        ),
        migrations.AlterField(
            model_name='rankregister',
            name='rank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ranking.Rank', verbose_name='assigned rank'),
        ),
    ]