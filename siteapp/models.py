# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
def upload_location(instance, filename):
	return '%s/%s' %(instance.album, filename)

class Bilde(models.Model):
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=140)
	album = models.CharField(max_length=20)
	image = models.ImageField(upload_to=upload_location, null=True, blank=True,width_field='width_field', height_field='height_field')
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)

def upload_location2(instance, filename):
	return '%s/%s' %('main', filename)

class Main_site(models.Model):
	title = models.CharField(max_length=30)
	image_text = models.CharField(max_length=140)
	text = models.TextField()
	image = models.ImageField(upload_to=upload_location2, null=True, blank=True,width_field='width_field', height_field='height_field')
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	POSITION_CHOICES = (
		('Over','Over'),
		('Under','Under')
	)
	position = models.CharField(max_length=6, choices=POSITION_CHOICES,default='Over')