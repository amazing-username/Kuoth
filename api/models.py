from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    year = models.IntegerField()
    genre = models.CharField(max_length=30)
    duration = models.IntegerField()
    filename = models.CharField(max_length=75)
    song_path = models.CharField(max_length=500)
