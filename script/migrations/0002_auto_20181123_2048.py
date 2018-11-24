# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-23 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('script', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='external_name',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='pythonscript',
            name='name',
            field=models.TextField(unique=True, verbose_name='脚本名字'),
        ),
    ]