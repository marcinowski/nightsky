"""
:created on: 2017-09-01

:author: Marcin Muszynski
:contact: marcinowski007@gmail.com
"""
from django.db import models


class Star(models.Model):
    hip = models.IntegerField(verbose_name="Hipparcos reference number", null=True)
    proper = models.CharField(verbose_name="Common name", max_length=32, null=True, blank=True)
    ra = models.FloatField(verbose_name="Right Ascension", null=True)
    dec = models.FloatField(verbose_name="Declination", null=True)
    dist = models.FloatField(verbose_name="Distance [pc]", null=True)
    mag = models.FloatField(verbose_name="Apparent visual magnitude", null=True)
    absmag = models.FloatField(verbose_name="Absolute visual magnitude", null=True)
    spect = models.CharField(verbose_name="Spectral type", max_length=16, null=True, blank=True)
