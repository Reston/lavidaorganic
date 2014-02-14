from django.db import models
from django.dispatch import receiver
from paypal.standard.ipn.signals import payment_was_successful, payment_was_flagged

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
		print ipn_obj.payer_email
		print ipn_obj.first_name
	elif ipn_obj.item_name == 'Consulta Personalizada' and ipn_obj.mc_gross == '149.99':
		#ENVIAR CORREO
		print ipn_obj.payer_email
		print ipn_obj.first_name
	return

@receiver(payment_was_flagged)
def payment_flagged(sender, **kwargs):
    print "FLAGGED: %s" % sender.payer_email

print "signals fueron importadas"


class CorreoBoletin(models.Model):
	""""Lista de correos ingresados por los clientes en la pagina de inicio para el boletin"""
	correo = models.EmailField(max_length=50)