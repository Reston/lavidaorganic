from django.contrib import admin

from .models import CorreoBoletin
from actions import export_as_csv_action


class CorreoBoletinAdmin(admin.ModelAdmin):
	"""Admin del modelo de correos de suscripcion"""
	list_display = ('correo',)
	search_fields= ['correo']
	actions = [export_as_csv_action("CSV Export", fields=['correo'])]

admin.site.register(CorreoBoletin, CorreoBoletinAdmin)