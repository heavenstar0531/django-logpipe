# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-04 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200)),
                ('partition', models.PositiveIntegerField()),
                ('offset', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('topic', 'partition', 'offset'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='offset',
            unique_together=set([('topic', 'partition')]),
        ),
    ]
