#!/usr/local/bin/python
# -*- encoding: utf-8 -*-
from django import forms
from .models import CorreoBoletin, HistoriaNutricional

class contactForm(forms.Form):
	nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Su nombre'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': ' nick@email.com'}))
	telefono = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Su Número de teléfono'}))
	texto = forms.CharField(widget=forms.Textarea)

	def clean_asunto(self):
		cd = self.cleaned_data
		asunto = cd.get('asunto')
		if len(asunto) < 3:
			raise forms.ValidationError("El asunto debe tener mas de 2 letras")
		return asunto

	def clean_texto(self):
		cd = self.cleaned_data
		texto = cd.get('texto')
		if len(texto) < 4:
			raise forms.ValidationError("*")
		return texto

class boletinForm(forms.ModelForm):
	correo = forms.EmailField(widget=forms.TextInput())

	class Meta:
		model = CorreoBoletin
		fields = ['correo']

class historiaNutricionalForm(forms.ModelForm):
	SINO = (('si','Si'),('no','No'))
	peso_sino = forms.ChoiceField(choices=SINO, widget=forms.RadioSelect())
	levanta_noche_sino = forms.ChoiceField(choices=SINO, widget=forms.RadioSelect())
	dolor_inflamacion_sino = forms.ChoiceField(choices=SINO, widget=forms.RadioSelect())
	estrenimiento_sino = forms.ChoiceField(choices=SINO, widget=forms.RadioSelect())
	alergia_sino = forms.ChoiceField(choices=SINO, widget=forms.RadioSelect())
	dolorperiodo_sino = forms.ChoiceField(choices=SINO, widget=forms.RadioSelect(), required=False)
	infecciones_sino = forms.ChoiceField(choices=SINO, widget=forms.RadioSelect(), required=False)
	suplementos_sino = forms.ChoiceField(choices=SINO, widget=forms.RadioSelect())
	pastillas_sino =forms.ChoiceField(choices=SINO, widget=forms.RadioSelect(), required=False)
	molestias = forms.CharField(widget=forms.Textarea())
	meta = forms.CharField(widget=forms.Textarea()) 
	punto_vida = forms.CharField(widget=forms.Textarea())
	enfermedad = forms.CharField(widget=forms.Textarea())
	salud_madre = forms.CharField(widget=forms.Textarea())
	soporte_amigos = forms.CharField(widget=forms.Textarea())
	comidas_mal = forms.CharField(widget=forms.Textarea())
	descansar_definicion = forms.CharField(widget=forms.Textarea())
	adicciones = forms.CharField(widget=forms.Textarea())
	cambiar_dieta = forms.CharField(widget=forms.Textarea())
	algo_mas = forms.CharField(widget=forms.Textarea())
	desayuno_infancia = forms.CharField(widget=forms.Textarea())
	almuerzo_infancia = forms.CharField(widget=forms.Textarea())
	cena_infancia = forms.CharField(widget=forms.Textarea())
	merienda_infancia = forms.CharField(widget=forms.Textarea())
	liquido_infancia = forms.CharField(widget=forms.Textarea())
	desayuno_actual = forms.CharField(widget=forms.Textarea())
	almuerzo_actual = forms.CharField(widget=forms.Textarea())
	cena_actual = forms.CharField(widget=forms.Textarea())
	merienda_actual = forms.CharField(widget=forms.Textarea())
	liquido_actual = forms.CharField(widget=forms.Textarea())

	class Meta:
		model = HistoriaNutricional		
