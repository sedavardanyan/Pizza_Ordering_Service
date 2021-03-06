# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-16 19:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='orders.Customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='pizza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.Pizza'),
        ),
    ]
