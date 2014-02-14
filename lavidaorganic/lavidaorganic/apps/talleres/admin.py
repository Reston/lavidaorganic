from django.contrib import admin
from .models import Taller
from .forms import TallerForm

class TallerAdmin(admin.ModelAdmin):
	form = TallerForm

admin.site.register(Taller, TallerAdmin)