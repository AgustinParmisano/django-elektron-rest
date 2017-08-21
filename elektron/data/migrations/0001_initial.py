# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 01:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_value', models.CharField(blank=True, default='0', max_length=100)),
                ('date', models.DateTimeField(default='0')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.Device')),
            ],
            options={
                'ordering': ('date',),
            },
        ),
    ]
