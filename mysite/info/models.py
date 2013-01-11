#coding=utf-8

from django.db import models
from django.contrib.auth.models import User

class Data(models.Model):
	name = models.CharField(max_length="500")
	surname = models.CharField(max_length="500")
	birth = models.DateField()
	bio = models.TextField(blank = True, null = True)
	email = models.EmailField(blank = True, null = True)
	jabber = models.CharField(max_length="500")		
	skype = models.CharField(max_length="500")
	other_contacts = models.TextField(blank = True, null = True)

	class Meta:
		verbose_name = "Artykuł"
		verbose_name_plural = "Artykuły"

	def __str__(self):
		return u'%s' % (self.name)
	
	def __unicode__(self):
		return self.__str__()