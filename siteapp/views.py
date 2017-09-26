# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Count
from django.shortcuts import render
from .models import Bilde, Main_site

# Create your views here.

def album(request):
	albumListe = Bilde.objects.values('album').annotate(total=Count('album')).all()
	bildeListe = {}
	curAlb = albumListe[0]['album']
	for album in albumListe:
		bildeListe[album['album']] = Bilde.objects.filter(album=album['album']).all()
		if request.GET.get('album') == album['album']:
			curAlb = album['album']
	bildeListe = bildeListe[curAlb]
	context={
		'title': 'Album',
		'albumListe': albumListe,
		'bildeListe': bildeListe,
	}
	return render(request, 'album.html', context)

def forside(request):
	over = Main_site.objects.filter(position='Over').all()
	under = Main_site.objects.filter(position='Under').all()
	context ={
		'over': over,
		'under': under,
		'title': 'Main'

	}
	return render(request,'home.html',context)

def undervann(request):

	context={
		'element': element,
		'title': 'Under vann'
	}

