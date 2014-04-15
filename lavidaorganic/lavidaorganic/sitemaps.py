#-*- encoding: utf-8 -*-
from django.contrib import sitemaps
from django.core.urlresolvers import reverse
from lavidaorganic.apps.talleres.models import Taller


class StaticViewSitemap(sitemaps.Sitemap):
	priority = 0.5
	changefreq = 'daily'

	def items(self):
		return [
				'homepageindex',
				'homepageabout',
				'homepageservices',
				'homapagecontact'
				]

	def location(self, item):
		return reverse(item)


class TallerSitemap(sitemaps.Sitemap):
	changefreq = 'daily'
	priority = 0.8

	def items(self):
		return Taller.objects.all()

	def lastmod(self, obj):
		return obj.modificado_en
