#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from lavidaorganic import settings
from lavidaorganic.apps.homepage.forms import contactForm
from django.template import RequestContext
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from zinnia.models import Entry
from lavidaorganic.apps.talleres.models import Taller
import nltk


def index(request):
	entradas= Entry.objects.order_by('-creation_date')
	entradas= entradas[:3]
	talleres = Taller.objects.order_by('-fecha')
	talleres= talleres[:3]
	for ent in entradas:
		quitar_html= nltk.clean_html(ent.content) 
		ent.content =  quitar_html[:100]
	ctx = {'entradas':entradas, 'talleres':talleres}	
	return render_to_response('homepage/index.html',ctx, context_instance=RequestContext(request))


def about(request):
	mision = "misión de la empresa"
	vision = "visión de la empresa"
	ctx = {'mision': mision, 'vision': vision}
	return render_to_response('homepage/sobregiselle.html', ctx, context_instance=RequestContext(request))


def services(request):
	# What you want the button to do.
	#Una Consulta Personalizada
	paypal_dict_consulta = {
		"business": "lavidaorganic@lavidaorganic.com",
		"amount": "149.99",
		"item_name": "Consulta Personalizada",
		"notify_url": "http://186.188.118.110:80/paypalito-manager/",
		"return_url": "http://186.188.118.110:80/historia-de-salud/",
		"cancel_return": "http://186.188.118.110:80/",

	}
	#Asesorio personalizada
	paypal_dict_asesoria = {
		"business": "lavidaorganic@lavidaorganic.com",
		"amount": "199.99",
		"item_name": "Asesoria Completa Personalizada",
		"notify_url": "http://186.188.118.110:80/paypalito-manager/",
		"return_url": "http://186.188.118.110:80/historia-de-salud/",
		"cancel_return": "http://186.188.118.110:80/",
	}

	# Create the instance.
	form_consulta = PayPalPaymentsForm(initial=paypal_dict_consulta)
	form_asesoria = PayPalPaymentsForm(initial=paypal_dict_asesoria)
	context = {'form_consulta': form_consulta, 'form_asesoria': form_asesoria}
	return render_to_response('homepage/servicios.html', context, context_instance=RequestContext(request))

@csrf_exempt
def historia(request):
	return render_to_response('homepage/historia.html', context_instance=RequestContext(request))

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

