# -*- encoding: utf-8 -*-
from django.db import models
from django.dispatch import receiver
from paypal.standard.ipn.signals import payment_was_successful, payment_was_flagged
from django.core.mail import send_mail
from lavidaorganic.apps.talleres.models import Usuario, PagoTaller, Taller
from django.conf  import settings

@receiver(payment_was_successful)
def show_me_the_money(sender, **kwargs):
	ipn_obj = sender
	print "CONFIRMED PAYMENT payment_was_successful"
	print ipn_obj
	print "========================================"
	if ipn_obj.item_name == 'Asesoria Completa Personalizada' and ipn_obj.mc_gross == '249.99':
		#ENVIAR CORREO
		mensaje = u'Gracias por realizar el pago para la Asesoria Completa Personalizada\n Pago realizado por: 199.99 $\n Para continuar con los pasos para realizar la Asesoria'
		+ 'debe ir a la siguiente dirección para llenar la historia de salud que sería el segundo paso por completar.\n Enlace para la historia: http://lavidaorganic.com/historia-de-salud/ '
		send_mail('Pago recibido por La Vida Organica - Asesoria Completa Personalizada', mensaje, settings.EMAIL_HOST_USER, [ipn_obj.payer_email], fail_silently=False)
		#print ipn_obj.payer_email
		#print ipn_obj.first_name

	elif ipn_obj.item_name == 'Consulta Personalizada' and ipn_obj.mc_gross == '149.99':
		#ENVIAR CORREO
		mensaje = u'Gracias por realizar el pago para la Consulta Personalizada\n Pago realizado por: 149.99 $\n Para continuar con los pasos para realizar la Consulta \
		debe ir a la siguiente dirección para llenar la historia de salud que sería el segundo paso por completar.\n Enlace para la historia: http://lavidaorganic.com/historia-de-salud/ '
		send_mail('Pago recibido por La Vida Organica - Consulta Personalizada', mensaje, settings.EMAIL_HOST_USER, [ipn_obj.payer_email], fail_silently=False)
	else:
		#Chequear si taller pagado existe
		try:
			taller_comprado = Taller.objects.get(titulo=ipn_obj.item_name)
		except Taller.DoesNotExist:
			return
		# And that someone didn't tamper with the price
		if int(taller_comprado.precio) != int(ipn_obj.mc_gross):
			return
		# Chequear si existe el usuario en caso contrario crearlo
		try:
			customer = Usuario.objects.get(email=ipn_obj.payer_email)
		except Usuario.DoesNotExist:
			customer = Usuario.objects.create(
			email=sender.payer_email,
			first_name=sender.first_name,
			last_name=sender.last_name
			)
		#Add a new order
		PagoTaller.objects.create(user=customer, taller=taller_comprado)
		#INCREMENTAR INSCRITOS
		inscribir(taller_comprado)
		print "Inscrito persona"
		#ENVIAR CORREO
		mensaje = 'Gracias por realizar el pago por '+str(taller_comprado.titulo)+'\n Pago realizado por: '+str(ipn_obj.mc_gross)+'$\n Pautado para la siguiente fecha: '+str(taller_comprado.fecha)+'\n Un dia antes de la fecha pautada se le enviara las instrucciones para asistir al '+str(taller_comprado.tipo)+'\n'
		if taller_comprado.tipo == 'Taller':
			mensaje = mensaje + 'Lugar: '+str(taller_comprado.lugar)+'\n Hora: '+str(taller_comprado.hora_hasta)
		send_mail('Pago recibido por La Vida Organica - '+taller_comprado.titulo, mensaje, settings.EMAIL_HOST_USER, [ipn_obj.payer_email], fail_silently=False)
		pass
	return

@receiver(payment_was_flagged)
def payment_flagged(sender, **kwargs):
	print "FLAGGED: %s" % sender.payer_email

print "signals fueron importadas"

def inscribir(taller_comprado):
	taller_comprado.inscritos = taller_comprado.inscritos + 1
	taller_comprado.save()
	return


class CorreoBoletin(models.Model):
	""""Lista de correos ingresados por los clientes en la pagina de inicio para el boletin"""
	correo = models.EmailField(max_length=50)

class HistoriaNutricional(models.Model):
	ESTADO_CIVIL = (('soltero','Soltero'), ('enrelacion','En una relación'), ('casado','Casado'), ('viudo','Viudo'), ('divorsiado','Divorsiado'),)
	TIPO_SANGRE = (('O-','O-'),('O+','O+'),('A-','A-'),('A+','A+'),('B-','B-'),('B+','B+'),('Ab-','Ab-'),('Ab+','Ab+'))
	PESO_METRICA = (('kg','Kilogramos'),('lb','Libras'))
	GENERO = (('femenino','Femenino'), ('masculino','Masculino'),)
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	direccion = models.CharField(max_length=200)
	frecuencia_email = models.CharField(max_length=100)
	telefono = models.CharField(max_length=100)
	fecha_nacimiento = models.DateField()
	lugar_nacimiento = models.CharField(max_length=200)
	estatura =  models.FloatField(default = 0)
	peso_actual =  models.FloatField(default = 0)
	peso_seismeses =  models.FloatField(default = 0)
	peso_lastyear =  models.FloatField(default = 0)
	peso_metrica = models.CharField(max_length=2, choices=PESO_METRICA, default ='kg')
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
	dolor_inflamacion = models.TextField()
	estrenimiento = models.TextField()
	alergia = models.TextField() 
	genero = models.CharField(max_length=20, choices=GENERO)
	periodo_regular = models.BooleanField(default=False)
	dias_periodo = models.IntegerField(null=True, blank=True)
	frecuencia_periodo = models.CharField(max_length=200, null=True, blank=True)
	sintomas_periodo = models.TextField(null=True, blank=True)
	menopausia = models.CharField(max_length=200, null=True, blank=True)
	pastillas_anticonceptivas = models.TextField(null=True, blank=True)
	infecciones_vaginales = models.TextField(null=True, blank=True)
	suplementos = models.TextField()
	terapia_sanadora = models.TextField()
	rol_deporte = models.TextField()
	alimentacion_infancia = models.TextField()
	alimentacion_actual = models.TextField()
	cocina = models.BooleanField(default=False)
	informacion_alimentacion = models.TextField()
	comida_casa = models.CharField(max_length=200)

