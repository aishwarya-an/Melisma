# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Song(models.Model):
  name = models.CharField(max_length = 20)
  singer = models.CharField(max_length = 20)
  duration = models.DurationField()

class Album(models.Model):
  name = models.CharField(max_length = 20)
  songlist = models.ManyToManyField(Song)


