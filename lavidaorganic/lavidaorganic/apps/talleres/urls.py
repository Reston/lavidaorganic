from django.conf.urls import patterns, url

urlpatterns = patterns(
	'lavidaorganic.apps.talleres.views',
	url(r'^talleres/$', 'talleres', name="tallerestalleres"),
	url(r'^talleres/(?P<titulo>[-\w]+)/$', 'taller', name="taller"),
)
