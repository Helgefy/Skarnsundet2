# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 09:41
from __future__ import unicode_literals

from django.db import migrations, models
import siteapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bilde',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=140)),
                ('album', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=siteapp.models.upload_locationB, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Main_site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image_text', models.CharField(max_length=140)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=siteapp.models.upload_locationM, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('position', models.CharField(choices=[('Over', 'Over'), ('Under', 'Under')], default='Over', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Under_vann',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image_text', models.CharField(max_length=140)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=siteapp.models.upload_locationB, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
            ],
        ),
    ]
