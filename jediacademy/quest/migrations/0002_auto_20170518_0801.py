# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 08:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'answer', 'verbose_name_plural': 'answers'},
        ),
        migrations.AlterModelOptions(
            name='exam',
            options={'verbose_name': 'exam', 'verbose_name_plural': 'exams'},
        ),
        migrations.AlterModelOptions(
            name='quest',
            options={'verbose_name': 'quest', 'verbose_name_plural': 'quests'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'task', 'verbose_name_plural': 'tasks'},
        ),
        migrations.AlterField(
            model_name='answer',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quest.Exam'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quest.Task'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reception.Person'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='rank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ranking.Rank'),
        ),
        migrations.AlterField(
            model_name='task',
            name='quest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quest.Quest'),
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together=set([('exam', 'task')]),
        ),
    ]