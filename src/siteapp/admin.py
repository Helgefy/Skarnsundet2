# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Bilde

class BildeAdmin(admin.ModelAdmin):
	list_display = ['name','album']
	list_display_links = ['name']
	list_filter = ['album']
	search_fields = ['name']
	class Meta:
		model = Bilde

admin.site.register(Bilde, BildeAdmin)