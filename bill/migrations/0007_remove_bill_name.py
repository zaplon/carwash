# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-24 08:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0006_remove_bill_vat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='name',
        ),
    ]
