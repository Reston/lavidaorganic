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
		mensaje = u'Gracias por realizar el pago para la Asesoria Completa Personalizada\n Pago realizado por: 199.99 $\n Para continuar con los pasos para realizar la Asesoria \
		debe ir a la siguiente dirección para llenar la historia de salud que sería el segundo paso por completar.\n Enlace para la historia: http://lavidaorganic.com/historia-de-salud/ '
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
	return

@receiver(payment_was_flagged)
def payment_flagged(sender, **kwargs):
    print "FLAGGED: %s" % sender.payer_email

print "signals fueron importadas"


class CorreoBoletin(models.Model):
	""""Lista de correos ingresados por los clientes en la pagina de inicio para el boletin"""
	correo = models.EmailField(max_length=50)