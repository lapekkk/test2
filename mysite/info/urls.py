from django.conf.urls.defaults import *
from views import *
from django.views.generic.simple import direct_to_template
from settings import MEDIA_ROOT
# coding=utf-8 

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', home),
)
