# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hip', models.IntegerField(verbose_name='Hipparcos reference number')),
                ('proper', models.SlugField(verbose_name='Common name')),
                ('ra', models.FloatField(verbose_name='Right Ascension [deg]')),
                ('dec', models.FloatField(verbose_name='Declination [deg]')),
                ('dist', models.FloatField(verbose_name='Distance [pc]')),
                ('mag', models.FloatField(verbose_name='Apparent visual magnitude')),
                ('absmag', models.FloatField(verbose_name='Absolute visual magnitude')),
                ('spect', models.SlugField(verbose_name='Spectral type')),
            ],
        ),
    ]
