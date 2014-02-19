# -*- encoding: utf-8 -*-
from django.db import models
from django.dispatch import receiver
from paypal.standard.ipn.signals import payment_was_successful, payment_was_flagged
from django.core.mail import send_mail

@receiver(payment_was_successful)
def show_me_the_money(sender, **kwargs):
	ipn_obj = sender
	print "CONFIRMED PAYMENT payment_was_successful"
	print ipn_obj
	print "========================================"
	print ipn_obj.item_name #ITEM NAME
	print ipn_obj.mc_gross #cantidad pagada
	if ipn_obj.item_name == 'Asesoria Completa Personalizada' and ipn_obj.mc_gross == '199.99':
		#ENVIAR CORREO
		mensaje = u'Gracias por realizar el pago para la Asesoria Completa Personalizada\n Pago realizado por: 199.99 $\n Para continuar con los pasos para realizar la Asesoria'
		+ 'debe ir a la siguiente dirección para llenar la historia de salud que sería el segundo paso por completar.\n Enlace para la historia: http://lavidaorganic.com/historia-de-salud/ '
		send_mail('Pago recibido por La Vida Organica - Asesoria Completa Personalizada', mensaje, 'ventas@lavidaorganic.com', [ipn_obj.payer_email], fail_silently=False)
		#print ipn_obj.payer_email
		#print ipn_obj.first_name

	elif ipn_obj.item_name == 'Consulta Personalizada' and ipn_obj.mc_gross == '149.99':
		#ENVIAR CORREO
		mensaje = u'Gracias por realizar el pago para la Consulta Personalizada\n Pago realizado por: 149.99 $\n Para continuar con los pasos para realizar la Consulta \
		debe ir a la siguiente dirección para llenar la historia de salud que sería el segundo paso por completar.\n Enlace para la historia: http://lavidaorganic.com/historia-de-salud/ '
		send_mail('Pago recibido por La Vida Organica - Consulta Personalizada', mensaje, 'ventas@lavidaorganic.com', [ipn_obj.payer_email], fail_silently=False)
		#print ipn_obj.payer_email
		#print ipn_obj.first_name
	else:
		#Aquí se debe realizar lo necesario pasa saber si pago bien un taller, el precio que es y registrar el usuario a ese taller.
		pass
	return

@receiver(payment_was_flagged)
def payment_flagged(sender, **kwargs):
    print "FLAGGED: %s" % sender.payer_email

print "signals fueron importadas"


class CorreoBoletin(models.Model):
	""""Lista de correos ingresados por los clientes en la pagina de inicio para el boletin"""
	correo = models.EmailField(max_length=50)

class HistoriaNutricional(models.Model):
	ESTADO_CIVIL = (('soltero','Soltero'), ('enrelacion','En una relación'), ('casado','Casado'), ('viudo','Viudo'), ('divorsiado','Divorsiado'),)
	TIPO_SANGRE = (('O-','O-'),('O+','O+'),('A-','A-'),('A+','A+'),('B-','B-'),('B+','B+'),('Ab-','Ab-'),('Ab+','Ab+'))
	PESO_METRICA = (('lb','Libras'),('kg','Kilogramos'),)
	GENERO = (('femenino','Femenino'), ('masculino','Masculino'),)
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	direccion = models.CharField(max_length=200)
	email = models.EmailField(max_length=50)
	frecuencia_email = models.CharField(max_length=100)
	telefono = models.CharField(max_length=100)
	fecha_nacimiento = models.DateField()
	lugar_nacimiento = models.CharField(max_length=200)
	estatura =  models.FloatField(default = 0)
	peso_actual =  models.FloatField(default = 0)
	peso_seismeses =  models.FloatField(default = 0)
	peso_lastyear =  models.FloatField(default = 0)
	peso_metrica = models.CharField(max_length=2, choices=PESO_METRICA)
	desea_rebajar = models.TextField()
	estado_civil = models.CharField(max_length=20, choices=ESTADO_CIVIL)
	numero_hijos = models.CharField(max_length=100)
	mascota = models.BooleanField(default=False)
	ocupacion = models.CharField(max_length=200)
	horas_semana = models.IntegerField()
	informacion_salud = models.TextField()
	tipo_sangre = models.CharField(max_length=20, choices=TIPO_SANGRE)
	problemas_dormir = models.BooleanField(default=False)
	horas_duerme = models.CharField(max_length=200)
	levanta_noche = models.TextField()
	dolor_inflamacion = models.CharField(max_length=200)
	estrenimiento = models.TextField()
	alergia = models.TextField() 
	genero = models.CharField(max_length=20, choices=GENERO)
	periodo_regular = models.BooleanField(default=False)
	dias_periodo = models.IntegerField()
	frecuencia_periodo = models.CharField(max_length=200)
	sintomas_periodo = models.TextField()
	menopausia = models.CharField(max_length=200)
	pastillas_anticonceptivas = models.TextField()
	infecciones_vaginales = models.TextField()
	suplementos = models.TextField()
	terapia_sanadora = models.TextField()
	rol_deporte = models.TextField()
	alimentacion_infancia = models.TextField()
	alimentacion_actual = models.TextField()
	cocina = models.BooleanField(default=False)
	informacion_alimentacion = models.TextField()
	comida_casa = models.CharField(max_length=200)





