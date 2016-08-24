# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-03 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contractor',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='last_name',
        ),
        migrations.AddField(
            model_name='contractor',
            name='address',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contractor',
            name='city',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contractor',
            name='name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contractor',
            name='zipcode',
            field=models.CharField(default='', max_length=6),
            preserve_default=False,
        ),
    ]
