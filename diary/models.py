#coding: utf-8

from django.db import models
from django.contrib.auth.models import User

class Diary(models.Model):
	user    = models.ForeignKey(User)
	date    = models.DateField()
	content = models.TextField()

	def __unicode__(self):
		return u'%s - %s' % (self.user, self.date)

class Cover(models.Model):
	user = models.ForeignKey(User)
	year = models.CharField(max_length=4)
	month = models.CharField(max_length=2)
	imgurl = models.URLField()

	def __unicode__(self):
		return u'%s - %s - %s' % (self.user, self.year, self. month)
		

class Feed(models.Model):
	user = models.CharField(max_length=50)
	title = models.CharField(max_length=50)
	content = models.TextField()

	def __unicode__(self):
		return u'%s' % self.title