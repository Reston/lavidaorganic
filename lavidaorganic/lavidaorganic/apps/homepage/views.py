#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
#from lavidaorganic import settings
from lavidaorganic.apps.homepage.forms import contactForm, boletinForm, historiaNutricionalForm
from django.template import RequestContext
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from zinnia.models import Entry
from lavidaorganic.apps.talleres.models import Taller
import nltk
import datetime


def index(request):
	newsletter = True
	if request.method == 'POST':
		form = boletinForm(request.POST)
		if form.is_valid():
			form.save()
			newsletter = False
	else:
		form = boletinForm()
	entradas = Entry.objects.filter(status=2).order_by('-creation_date')
	entradas = entradas.exclude(start_publication__gte=datetime.date.today())
	entradas= entradas[:4]
	talleres =  Taller.objects.filter(fecha__gte=datetime.date.today()).order_by('fecha')
	numero_talleres = talleres.count()
	talleres= talleres[:3]
	for ent in entradas:
		quitar_html= nltk.clean_html(ent.content) 
		ent.content =  quitar_html[:100]
	ctx = {'entradas':entradas, 'talleres':talleres, 'form':form, 'newsletter':newsletter,'numero':numero_talleres}	
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
		"business": "quecomicovzla@gmail.com",
		"amount": "149.99",
		"item_name": "Consulta Personalizada",
		"notify_url": "http://lavidaorganic.com/paypalito-manager/",
		"return_url": "http://lavidaorganic.com/historia-de-salud/",
		"cancel_return": "http://lavidaorganic.com/",

	}
	#Asesorio personalizada
	paypal_dict_asesoria = {
		"business": "lavidaorganic@lavidaorganic.com",
		"amount": "249.99",
		"item_name": "Asesoria Completa Personalizada",
		"notify_url": "http://lavidaorganic.com/paypalito-manager/",
		"return_url": "http://lavidaorganic.com/historia-de-salud/",
		"cancel_return": "http://lavidaorganic.com/",
	}

	# Create the instance.
	form_consulta = PayPalPaymentsForm(initial=paypal_dict_consulta)
	form_asesoria = PayPalPaymentsForm(initial=paypal_dict_asesoria)
	context = {'form_consulta': form_consulta, 'form_asesoria': form_asesoria}
	return render_to_response('homepage/servicios.html', context, context_instance=RequestContext(request))

@csrf_exempt
def historia(request):
	success = False
	if request.method == 'POST':
		form = historiaNutricionalForm(request.POST)
		print form.errors
		if form.is_valid():
			success = True
			form.save()
			cd = form.cleaned_data
			contenido = crearEmail(cd)
			print contenido
			#asunto = u'Por: %s mail: %s Tipo de servicio: %s Plan: %s' % (cd['nombre'], cd['email'], cd['tipoServicio'], cd['planes'])
			#send_mail(asunto, content, cd['email'], ['xxxx@xxxxxx.com'])
	else:
		form = historiaNutricionalForm()
	ctx = {'form': form, 'success': success}
	return render_to_response('homepage/historia.html', ctx, context_instance=RequestContext(request))

def contact(request):
	success = False
	if request.method == 'POST':
		form = contactForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			asunto = u'Por: %s mail: %s Tipo de servicio: %s Plan: %s' % (cd['nombre'], cd['email'], cd['tipoServicio'], cd['planes'])
			content = u'Email contacto: %s \nAsunto: %s \nTelefono: %s \nDescripcion: %s' % (cd['email'], asunto, cd['telefono'], cd['texto'])
			send_mail(asunto, content, 'conctato@lavidaorganic.com', ['contacto@lavidaorganic.com'])
	else:
		form = contactForm()
	ctx = {'form': form, 'success': success}
	return render_to_response('homepage/contacto.html', ctx, context_instance=RequestContext(request))

def crearEmail(cd):
	metrica = cd['peso_metrica']
	p1, p2, p3, p4, p5, p6, p7,p8, p9, p10 = "","","","","","","","","",""
	if(cd['desea_rebajar'] != 'No'):
		p1 = 'Si. '
	if(cd['levanta_noche'] != 'No'):
		p3= 'Si. '
	if(cd['dolor_inflamacion'] != 'No'):
		p4= 'Si. '	
	if(cd['estrenimiento'] != 'No'):
		p5= 'Si. '	
	if(cd['alergia'] != 'No'):
		p6= 'Si. '	
	if(cd['sintomas_periodo'] != 'No'):
		p7= 'Si. '	
	if(cd['pastillas_anticonceptivas'] != 'No'):
		p8= 'Si. '	
	if(cd['infecciones_vaginales'] != 'No'):
		p9= 'Si. '
	if(cd['suplementos'] != 'No'):
		p10= 'Si. '

	if(cd['mascota']):
		mascota = 'si'
	else:
		mascota = 'no'
	if(cd['periodo_regular']):
		periodo = 'si'		
	else:
		periodo = 'no'
	if(cd['problemas_dormir']):
		problemas_dormir = 'si'
	else:
		problemas_dormir = 'no'		
	if(cd['cocina']):
		cocina = 'si'
	else:
		cocina = 'no'			
	contenido = u"Nombre: %s \n\n Apellido: %s \n\n Dirección:\n %s \n\n Frecuencia que revisa su email:\n %s \n\n Género:\n %s \n\n " %(cd['nombre'],cd['apellido'], cd['direccion'],cd['frecuencia_email'], cd['genero'])+\
	u"Fecha de Nacimiento:\n %s \n\n Lugar de Nacimiento:\n %s \n\nEstatura:\n %s metros. \n\n Peso Actual\n %s %s \n\n" % (cd['fecha_nacimiento'],cd['lugar_nacimiento'], cd['estatura'], cd['peso_actual'], metrica) +\
	u"Peso hace 6 meses:\n %s %s \n\nPeso hace 1 año:\n %s %s \n\n ¿Quiere que su peso sea diferente?\n %s %s\n\n"%(cd['peso_seismeses'],metrica,cd['peso_lastyear'],metrica, p1, cd['desea_rebajar'])+\
	u"Estado Civil:\n %s \n\nNúmero de Hijos:\n %s \n\nMascota: %s \n\n Ocupación:\n %s \n\nHoras a la semana (Ocupación):\n %s horas \n\n" % (cd['estado_civil'], cd['numero_hijos'], mascota, cd['ocupacion'], cd['horas_semana']) +\
	u"Información de salud:\n %s \n\n Tipo de sangre:\n %s \n\n Problemas para dormir:\n %s \n\n¿Cuantas horas duerme?\n %s horas \n\n" % (cd['informacion_salud'], cd['tipo_sangre'],problemas_dormir, cd['horas_duerme'])+\
	u"¿Se levanta en la noche?\n %s%s \n\n¿Tiene algún dolor/inflamación?\n %s%s \n\n¿Estreñimiento/Diarrea/Gas?\n %s%s \n\n¿Tiene alguna alergia o es sensitivo a algo?\n %s%s \n\n" %(p3, cd['levanta_noche'],p4,cd['dolor_inflamacion'],p5,cd['estrenimiento'],p6,cd['alergia'])+\
	u"¿Son sus periodos regulares?\n %s \n\n¿Cuantos dias le dura el periodo?\n %s días. \n\n¿Con que frecuencia?\n %s \n\n¿Tiene actualmente o casi llega a la menopausia?\n %s \n\n"%(periodo,cd['dias_periodo'], cd['frecuencia_periodo'], cd['menopausia'])+\
	u"¿Sus periodos son dolorosos?\n %s%s \n\n¿Historial de pastillas anticonceptivas?\n %s%s \n\n¿Experimenta infecciones vaginales o infecciones urinarias?\n %s%s \n\n" % (p7,cd['sintomas_periodo'],p8,cd['pastillas_anticonceptivas'],p9, cd['infecciones_vaginales'])+\
	u"¿Toma actualmente suplementos/medicamentos?\n %s%s \n\n¿Algúna terapia o actividad sanadora que esta haciendo?\n %s \n\n¿Que rol juega los deportes o actividad fisica en su vida?\n %s \n\n" %(p10,cd['suplementos'], cd['terapia_sanadora'], cd['rol_deporte'])+\
	u"Alimentación Infacia:\n %s \n\n Alimentación Actual:\n %s \n\n¿Cocina?\n %s \n\n¿Que porcentaje de la comida es en casa?\n %s \n\n Información Alimentación:\n %s \n\n"%(cd['alimentacion_infancia'], cd['alimentacion_actual'],cocina, cd['comida_casa'], cd['informacion_alimentacion'])
	return contenido