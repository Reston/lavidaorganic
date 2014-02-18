#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from lavidaorganic.apps.talleres.models import Taller
from paypal.standard.forms import PayPalPaymentsForm
from django.shortcuts import get_object_or_404
import datetime

def talleres(request):
	lista_talleres = Taller.objects.filter(fecha__gte=datetime.date.today()).order_by('fecha')
	#ALGORITMO PARA FILTRAR
	ctx = {'talleres': lista_talleres}
	return render_to_response('talleres/talleres.html', ctx, context_instance=RequestContext(request))


def taller(request, titulo):
	titulo = titulo.replace('_', ' ')
	taller = get_object_or_404(Taller, titulo=titulo)
	#Asesorio personalizada
	paypal_dict_taller = {
		"business": "lavidaorganic@lavidaorganic.com",
		"amount": taller.precio,
		"item_name": taller.titulo,
		"notify_url": "http://186.188.118.110:80/paypalito-manager/",
		"return_url": "http://186.188.118.110:80/historia-de-salud/",
		"cancel_return": "http://186.188.118.110:80/",
	}
	# Create the instance.
	form_taller = PayPalPaymentsForm(initial=paypal_dict_taller)
	ctx = {'taller': taller, 'form_taller':form_taller}
	return render_to_response('talleres/taller_detalle.html', ctx, context_instance=RequestContext(request))

