# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-20 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warhammer', '0007_auto_20180419_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='race',
            field=models.CharField(choices=[('human', 'human'), ('dwarf', 'dwarf'), ('elf', 'elf'), ('halfling', 'halfling')], default='human', max_length=16),
        ),
    ]
