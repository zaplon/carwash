# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('code', models.CharField(max_length=25)),
                ('price', models.FloatField()),
                ('vat', models.FloatField(default=0)),
            ],
        ),
    ]
