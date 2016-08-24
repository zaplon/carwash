# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-20 10:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicem2m',
            name='unit',
        ),
        migrations.RemoveField(
            model_name='servicem2m',
            name='vat',
        ),
        migrations.AlterField(
            model_name='servicem2m',
            name='discount',
            field=models.FloatField(blank=True, null=True, verbose_name='Zni\u017cka'),
        ),
        migrations.AlterField(
            model_name='servicem2m',
            name='price',
            field=models.FloatField(verbose_name='Cena jednostkowa brutto'),
        ),
        migrations.AlterField(
            model_name='servicem2m',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Service', verbose_name='Us\u0142uga'),
        ),
    ]
