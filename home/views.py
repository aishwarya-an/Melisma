# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from album.models import Album

def show_home(request):
  album_list = Album.objects.all().order_by('name')
  return render(request, 'home.html', {'albumlist': album_list})
