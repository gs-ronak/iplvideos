from datetime import date
from django.db import models
from django.template.defaultfilters import slugify

from taggit.managers import TaggableManager

class Video(models.Model):

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	heading = models.CharField(max_length=255, blank=True, null=True)
	sub_heading = models.CharField(max_length=255, blank=True, null=True)
	short_info = models.CharField(max_length=500, blank=True, null=True)
	source = models.CharField(max_length=500, blank=True, null=True)
	url = models.CharField(max_length=255)
	thumbnail = models.CharField(max_length=255, blank=True, null=True)

	views = models.IntegerField(blank=True, null=True)
	likes = models.IntegerField(blank=True, null=True)
	dislikes = models.IntegerField(blank=True, null=True)
	shares = models.IntegerField(blank=True, null=True)
	description = models.TextField()
	tags = TaggableManager()


	def __str__(self):
		return self.url

	def __unicode__(self):
		return self.url

