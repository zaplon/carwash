# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-22 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0004_auto_20160803_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='vat',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]