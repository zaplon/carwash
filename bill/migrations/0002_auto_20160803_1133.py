# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-03 11:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0002_auto_20160803_1131'),
        ('bill', '0001_initial'),
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceToBill',
            fields=[
                ('servicem2m_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='invoice.ServiceM2M')),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bill.Bill')),
            ],
            bases=('invoice.servicem2m',),
        ),
        migrations.AddField(
            model_name='bill',
            name='service',
            field=models.ManyToManyField(related_name='bills', through='bill.ServiceToBill', to='service.Service', verbose_name='Us\u0142ugi'),
        ),
    ]
