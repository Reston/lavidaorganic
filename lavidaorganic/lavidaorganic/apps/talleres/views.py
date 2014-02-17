#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from lavidaorganic.apps.talleres.models import Taller
from django.shortcuts import get_object_or_404
import datetime

def talleres(request):
	lista_talleres = Taller.objects.filter(fecha__gte=datetime.date.today()).order_by('fecha')
	#ALGORITMO PARA FILTRAR
	ctx = {'talleres': lista_talleres}
	return render_to_response('talleres/talleres.html', ctx, context_instance=RequestContext(request))


def taller(request, titulo):
	mensaje = ''
	titulo = titulo.replace('_', ' ')
	taller = get_object_or_404(Taller, titulo=titulo)
	ctx = {'taller': taller,}
	return render_to_response('talleres/taller_detalle.html', ctx, context_instance=RequestContext(request))

