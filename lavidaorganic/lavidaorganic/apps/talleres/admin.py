from django.contrib import admin
from .models import Taller, Usuario, PagoTaller
from lavidaorganic.apps.homepage.actions import export_as_csv_action

class TallerAdmin(admin.ModelAdmin):
	"""Admin de los talleres de la vida organica"""
	list_display = ('titulo', 'descripcion_corta', 'fecha', 'hora_hasta', 'precio', 'tipo', 'lugar',)
	search_fields = ['titulo', 'precio']
	list_filter = ['tipo', 'fecha']

class UsuarioAdmin(admin.ModelAdmin):
	"""Admin del modelo de usuarios de suscripcion"""
	list_display = ('first_name', 'last_name', 'email', 'creado_en', 'modificado_en',)
	search_fields = ['email', 'first_name', 'last_name']
	actions = [export_as_csv_action("CSV Export", fields=['email'])]

class PagoTallerAdmin(admin.ModelAdmin):
	"""Admin del modelo de pagos realizados de los usuarios"""		
	list_display = ('taller', 'user',)
	search_fields = ['taller__titulo', 'user__email']
	list_filter = ['taller']
	actions = [export_as_csv_action("CSV Export", fields=['user'])]

admin.site.register(Taller, TallerAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(PagoTaller, PagoTallerAdmin)
