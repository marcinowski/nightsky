# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='star',
            name='dec',
            field=models.FloatField(verbose_name='Declination'),
        ),
        migrations.AlterField(
            model_name='star',
            name='dist',
            field=models.FloatField(default=0.0, verbose_name='Distance [pc]'),
        ),
        migrations.AlterField(
            model_name='star',
            name='hip',
            field=models.IntegerField(default=0, verbose_name='Hipparcos reference number'),
        ),
        migrations.AlterField(
            model_name='star',
            name='proper',
            field=models.SlugField(default='', verbose_name='Common name'),
        ),
        migrations.AlterField(
            model_name='star',
            name='ra',
            field=models.FloatField(verbose_name='Right Ascension'),
        ),
        migrations.AlterField(
            model_name='star',
            name='spect',
            field=models.SlugField(default='', verbose_name='Spectral type'),
        ),
    ]