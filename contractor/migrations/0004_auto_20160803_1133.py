# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-03 11:33
from __future__ import unicode_literals

import contractor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractor', '0003_auto_20160803_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='nip',
            field=models.CharField(max_length=13, validators=[contractor.fields.validate_nip], verbose_name='NIP'),
        ),
    ]
