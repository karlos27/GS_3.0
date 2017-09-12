#!/usr/bin/python
# -*- coding: utf8 -*-
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms
from .models import perfil

class RegistreForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email',)
		labels = {'username': 'Nom usuari', 'first_name': 'Nom', 'last_name': 'Cognoms', 'email': 'Correu',}

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)
        labels = {'first_name':'Nom', 'last_name':'Cognoms', 'email':'Correu Electrònic',}
        widgets = {
        	'first_name':forms.TextInput(attrs={'class':'form-control'}),
        	'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }    

class PerfilForm(forms.ModelForm):
	class Meta:
		model = perfil
		fields = ('nif', 'direcc', 'pobl', 'telf_1', 'fax',)
		labels = {'nif':'NiF', 'direcc':'Direcció', 'pobl':'Ciutat', 'telf_1':'Tel.', 'fax':'Fax',}
		widgets = {
            'nif':forms.TextInput(attrs={'class':'form-control'}),
        	'direcc':forms.TextInput(attrs={'class':'form-control'}),
        	'pobl':forms.TextInput(attrs={'class':'form-control'}),
        	'telf_1':forms.TextInput(attrs={'class':'form-control'}),
        	'fax':forms.TextInput(attrs={'class':'form-control'}),
        }
