# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('heading', models.CharField(max_length=255, null=True, blank=True)),
                ('sub_heading', models.CharField(max_length=255, null=True, blank=True)),
                ('short_info', models.CharField(max_length=500, null=True, blank=True)),
                ('source', models.CharField(max_length=500, null=True, blank=True)),
                ('url', models.CharField(max_length=255)),
                ('thumbnail', models.CharField(max_length=255, null=True, blank=True)),
                ('views', models.IntegerField(null=True, blank=True)),
                ('likes', models.IntegerField(null=True, blank=True)),
                ('dislikes', models.IntegerField(null=True, blank=True)),
                ('shares', models.IntegerField(null=True, blank=True)),
                ('description', models.TextField()),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
