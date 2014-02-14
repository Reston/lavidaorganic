# coding: utf-8
from django.db import models
from tinymce.models import HTMLField
from django.core.urlresolvers import reverse


class Taller(models.Model):
	TIPO_CHOICES = (('taller', 'Taller Presencial'), ('webinar', 'Webinar',),)
	titulo = models.CharField(max_length=25, help_text='Hasta 25 caracteres y solamente alfanuméricos', unique=True)
	descripcion_corta = models.CharField(max_length=170, help_text='170 caracteres Para mostrar en página de inicio')
	descripcion = HTMLField()
	fecha = models.DateTimeField()
	hora_hasta = models.TimeField()
	precio = models.DecimalField(max_digits=19, decimal_places=2)
	tipo = models.CharField(choices=TIPO_CHOICES, max_length=20, default='taller')
	lugar = models.CharField(max_length=200, help_text='Hasta 200 caracteres, si es webinar dejar en blanco', blank=True)

	def __unicode__(self):
		return self.titulo

	def get_absolute_url(self):
		titulo = self.titulo.replace(' ', '_')
		return reverse('taller', kwargs={'titulo': titulo})