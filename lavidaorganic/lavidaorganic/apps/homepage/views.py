#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from lavidaorganic.apps.homepage.forms import contactForm
from django.template import RequestContext
from django.core.mail import send_mail
from zinnia.models import Entry
import nltk


def index(request):
	entradas= Entry.objects.order_by('-creation_date')
	entradas= entradas[:3]
	for ent in entradas:
		quitar_html= nltk.clean_html(ent.content) 
		ent.content =  quitar_html[:100]
	ctx = {'entradas':entradas}	
	return render_to_response('homepage/index.html',ctx, context_instance=RequestContext(request))


def about(request):
	mision = "misión de la empresa"
	vision = "visión de la empresa"
	ctx = {'mision': mision, 'vision': vision}
	return render_to_response('homepage/sobregiselle.html', ctx, context_instance=RequestContext(request))


def services(request):
	serv = "El arte de servir"
	ctx = {'serv': serv}
	return render_to_response('homepage/servicios.html', ctx, context_instance=RequestContext(request))


def contact(request):
	success = False
	if request.method == 'POST':
		form = contactForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			asunto = u'Por: %s mail: %s Tipo de servicio: %s Plan: %s' % (cd['nombre'], cd['email'], cd['tipoServicio'], cd['planes'])
			content = u'Email contacto: %s \nAsunto: %s \nTelefono: %s \nDescripcion: %s' % (cd['email'], asunto, cd['telefono'], cd['texto'])
			send_mail(asunto, content, cd['email'], ['xxxx@xxxxxx.com'])
	else:
		form = contactForm()
	ctx = {'form': form, 'success': success}
	return render_to_response('homepage/contacto.html', ctx, context_instance=RequestContext(request))
