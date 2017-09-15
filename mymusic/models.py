# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

class Playlist(models.Model):
  name = models.CharField(max_length = 30)
  user_id = models.ForeignKey(
      'mymusic.User', on_delete=models.CASCADE, related_name='playlists')
  songlist = models.ForeignKey('album.Song', on_delete = models.CASCADE)

class User(AbstractUser):
  pass
