# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-16 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20181116_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
