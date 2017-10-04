# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from .models import Bilde, Main_site, Under_vann, Htmlsite

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
	element = Under_vann.objects.all()
	context = {
		'element': element,
		'title': 'Under vann'
	}
	return render(request, 'blogside.html', context)

def htmlView(request):
	element = get_object_or_404(Htmlsite,slug=slug)
	context = {
		'title': element.name,
		'html': element.html
	}

	return render(request, 'htmlsite.html', context)