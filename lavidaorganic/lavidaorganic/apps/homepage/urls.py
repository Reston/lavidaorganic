from django.conf.urls import patterns, url

urlpatterns = patterns(
	'lavidaorganic.apps.homepage.views',
	url(r'^$', 'index', name="homepageindex"),
	url(r'^sobregiselle/$', 'about', name="homepageabout"),
	url(r'^servicios/$', 'services', name="homepageservices"),
	url(r'^contacto/$', 'contact', name="homapagecontact"),
)
