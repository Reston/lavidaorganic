#!/usr/local/bin/python
# -*- encoding: utf-8 -*-
from django import forms
from .models import CorreoBoletin

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
