# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django import forms
# Register your models here.
from .models import Bilde, Main_site, Htmlsite

class BildeAdmin(admin.ModelAdmin):
	list_display = ['name','album']
	list_display_links = ['name']
	list_filter = ['album']
	search_fields = ['name']
	class Meta:
		model = Bilde

class MainAdmin(admin.ModelAdmin):
	list_display= ['title','position']
	list_display_links = ['title']
	list_filter = ['position']
	class Meta:
		model = Main_site


class HtmlAdmin(admin.ModelAdmin):
	list_display = ['name']
	list_display_links = ['name']
	class Meta:
		model = Htmlsite



admin.site.register(Bilde, BildeAdmin)
admin.site.register(Main_site, MainAdmin)
admin.site.register(Htmlsite,HtmlAdmin)