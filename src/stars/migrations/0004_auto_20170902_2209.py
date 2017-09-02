# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stars', '0003_auto_20170902_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='star',
            name='hip',
            field=models.IntegerField(null=True, verbose_name='Hipparcos reference number'),
        ),
        migrations.AlterField(
            model_name='star',
            name='proper',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Common name'),
        ),
        migrations.AlterField(
            model_name='star',
            name='spect',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Spectral type'),
        ),
    ]