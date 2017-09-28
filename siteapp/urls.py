from django.conf.urls import url
from django.contrib import admin

from .views import(
	album,
	forside,
	undervann,
	)

urlpatterns = [
    url(r'^$', forside,name='main'),
    url(r'^album/$', album,name='album'),
    url(r'^under_vann/$',undervann, name='undervann'),
]