# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#Red pk 1
class Album(models.Model):
	artist=models.Charfield(max_length=250)
	album_title=models.Charfield(max_length=250)
	album_logo= models.Charfield(max_length=250)
	genremodels.Charfield(max_length=100)

class Song(models.Model):
	album=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type= models.Charfield(max_length=10)
    song_title=models.Charfield(max_length=250)
    