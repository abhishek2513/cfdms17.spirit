# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_type', models.CharField(max_length=25)),
                ('item_name', models.CharField(max_length=50)),
            ],
        ),
    ]
